from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=12, null=True)
    email = models.EmailField(unique=True)
    biografia = models.TextField(null=True, blank=True)
    ROLE_CHOICES = (
         ('professor', 'professor'),
         ('aluno', 'aluno'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    imagem = models.ImageField(upload_to='foto_perfil/' , default='foto_perfil/default.png', null=True, blank=True)
    ANO_CHOICES = (
        ('1_EM', '1º Ano Ensino Médio'),
        ('2_EM', '2º Ano Ensino Médio'),
        ('3_EM', '3º Ano Ensino Médio'),
        ('4_EM', '4º Ano Ensino Médio'),
    )
    ano_escolar = models.CharField(max_length=20, choices=ANO_CHOICES, null=True, blank=True)
    escola = models.CharField(max_length=50, null=True, blank=True)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name']

