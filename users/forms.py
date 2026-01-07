from django import forms
from .models import Usuario

class Registerform(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','first_name','last_name', 'email', 'role', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['imagem','username', 'first_name', 'last_name', 'telefone','biografia', 'escola', 'ano_escolar']