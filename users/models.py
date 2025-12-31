from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=12, null=True)
    email = models.EmailField(unique=True)
    biografia = models.TextField(null=True, blank=True)
    # ROLE_CHOICES = (
    #     ('professor', 'professor'),
    #     ('aluno', 'aluno'),
    # )
    # role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name']

