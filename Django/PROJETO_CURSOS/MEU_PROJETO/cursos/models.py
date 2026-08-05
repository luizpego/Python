from django.db import models
# Create your models here.

class Curso(models.Model):
    titulo = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    publicado = models.BooleanField(default=False)
    descricao = models.TextField()
    professor = models.ForeignKey('Professor', models.CASCADE)
    link = models.URLField(null=True)

class Professor(models.Model):
    nome = models.CharField(max_length=40)
    salario = models.DecimalField(max_digits=7, decimal_places=2)

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.ForeignKey('Curso', models.CASCADE,null=True)
    matriculado = models.BooleanField(default=False)



