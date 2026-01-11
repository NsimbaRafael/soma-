from django.shortcuts import render, redirect
from  .forms import Registerform, LoginForm, UserUpdateForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role
from django.core.mail import send_mail

# Create your views here.
def registerView(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            #Criamos o objecto mas ainda não salvamos no banco de dados
            user = form.save(commit=False)
            # Criptografando palavra passe
            user.set_password(form.cleaned_data['password'])
            user.save()
            send_mail(
                    subject='Inicio de sessão',
                    message=f' Sr.{user.username}, Seja bem vindo ao teu ToDoList, agora poderás gerencia melhor as tuas tarefas, sempre que esquecer, a tua app fará questão de lembrar-te',
                    from_email='daskapp26@gmail.com',
                    recipient_list=[user.email],
                   fail_silently=False
             )

            selected_role = form.cleaned_data.get('role')
            if selected_role:
                 assign_role(user, selected_role)
            messages.success(request, 'Conta criada com sucesso')
            return redirect('sigin')
    else:
        form = Registerform()    
    return render(request, 'auth/register.html', {'form':form})    


        


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
                return redirect(profile)
            else:
                messages.error(request, "Email ou senha errados")
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form':form})


def logout_views(request):
    logout(request)
    return redirect('sigin')

@login_required
def profile(request):
    return render(request, 'profile/profile.html')



@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'O seu perfil foi atualizado com sucesso')
            return redirect(profile)
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request,'profile/update_profile.html', context)
        