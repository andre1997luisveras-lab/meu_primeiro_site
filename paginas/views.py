from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    contexto = {
        "nome": "André Luís",
        "cidade": "Rio de Janeiro",
        "morando": "Pernambuco",
        "cursos": ["Python", "Django", 2 , 1],
        "hobbies": ["Jogar", "Comer", "Dormir", "Ver filmes"],
    }
    return render(request, "inicio.html", contexto)


def sobre(request):
    return render(request, "sobre.html", sobre)


def contato(request):
    return render(request, "contato.html")