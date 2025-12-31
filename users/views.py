from django.shortcuts import render, redirect
from  .forms import Registerform, LoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role

# Create your views here.
def registerView(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            #Criamos o objectivo mas ainda não salvamos no banco de dados
            user = form.save(commit=False)
            # Criptografando palavra passe
            user.set_password(form.cleaned_data['password'])
            user.save()

            # selected_role = form.cleaned_data.get('role')
            # if selected_role:
            #     assign_role(user, selected_role)
            messages.success(request, 'Conta criada com sucesso')
            return redirect('sigin')
    else:
        form = Registerform()    
    return render(request, 'pages/auth/register.html', {'form':form})    
        


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # Tenta encontrar um usuário com essas credencias
            user = authenticate(request, username = email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Seja bem vindo{user.first_name}!")
                return redirect(homepage)
            else:
                messages.error(request, "Email ou senha errados")
    else:
        form = LoginForm()
    return render(request, 'pages/auth/login.html', {'form':form})

@login_required
def homepage(request):
    return render(request, 'pages/homepage.html')