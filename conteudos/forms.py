from django import forms
from .models import Material, Disciplina, Curso

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        # O autor não entra aqui, pois o pegaremos da sessão (request.user)
        fields = ['titulo', 'arquivo', 'curso', 'disciplina', 'ano_escolar']
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Resumo de Genética'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-select'}),
            'disciplina': forms.Select(attrs={'class': 'form-select'}),
            'ano_escolar': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aqui você pode customizar o queryset se quiser, por exemplo, 
        # ordenar as disciplinas por nome no formulário:
        self.fields['disciplina'].queryset = Disciplina.objects.all().order_by('nome')
        self.fields['curso'].queryset = Curso.objects.all().order_by('nome')