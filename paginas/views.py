from django.shortcuts import render
from django.http import HttpResponse
from .models import Livros, Categoria
from .models import Projetos


def inicio(request):
    contexto = {
        "nome": "André Luís",
        "cidade": "Rio de Janeiro",
        "morando": "Pernambuco",
        "cursos": ["Python", "Django", 2 , 1],
        "hobbies": ["Jogar", "Comer", "Dormir", "Ver filmes"],
    }

    return render(request, "inicio.html", contexto)

def projetos(request):
    projetos = {
        "projetos": Projetos.objects.all()
    }
    return render(request, "projetos.html", projetos)

def sobre(request):
    return render(request, "sobre.html",)

def contato(request):
    return render(request, "contato.html")

def categoria(request):
    contexto = {
        "categorias": Categoria.objects.all()
    }
    return render(request, "categoria.html", contexto)
