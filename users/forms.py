from django import forms
from .models import Usuario

class Registerform(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name','last_name', 'email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")