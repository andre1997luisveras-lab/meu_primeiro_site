from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    dados = {
        "nome": "André Luís",
        "idade": 29,
        "altura": 1.80,
        "pets": ["Nina", "Maya", "Billie"],
    }
    return render(request, "inicio.html", dados)

def sobre(request):
    return HttpResponse("<h1>Sobre mim</h1>"
                        "<p>Meu nome é André e estou aprendendo Django.</p>")



def contato(request):
    return HttpResponse(
        "<h1>Contatos</h1>"
        "<p>E-mail: andre1997luisveras@gmail.com</p>"
        "<a href='/'>Inicio</a> |   "
        "<a href='/sobre/'>Sobre</a>"
    )
