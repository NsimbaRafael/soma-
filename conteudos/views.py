from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator
from django.contrib import messages
from .forms import MaterialForm
from .models import Material

@login_required
@has_permission_decorator('upload_content')
def upload_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES) # request.FILES é obrigatório para arquivos!
        
        if form.is_valid():
            # Interrompemos o salvamento para adicionar o autor
            material = form.save(commit=False)
            material.author = request.user  # O autor é quem está logado
            material.save() # Agora sim salvamos no banco
            
            messages.success(request, 'Material compartilhado com sucesso no Soma+!')
            return redirect('lista_materiais') # Redireciona para a lista de conteúdos
    else:
        form = MaterialForm()
    
    return render(request, 'conteudos/upload.html', {'form': form})


@login_required
def lista_materiais(request):
    # Lógica: Pegar todos os materiais do mais novo para o mais antigo
    materiais =Material.objects.select_related('author', 'curso', 'disciplina').all().order_by('-data_criacao')
    return render(request, 'conteudos/lista.html', {'materiais': materiais})