from django.db import models

# Create your models here.

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    ano_publicacao = models.IntegerField()

class Projetos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    data_criacao = models.DateField()
    linguagem = models.CharField(max_length=50)
