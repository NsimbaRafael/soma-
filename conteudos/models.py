from django.db import models
from django.conf import settings

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')
    def __Str__(self):

        return  f"{self.nome} ({self.curso})"

class Material(models.Model):
    ANO_CHOiCES = (
        ('10', '10ª Classe'),
        ('11', '11ª Classe'),
        ('12', '12ª Classe'),
    )
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='materias/', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True)
    ano_escolar = models.CharField(max_length=30, choices=ANO_CHOiCES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

