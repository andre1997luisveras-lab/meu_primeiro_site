from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Projetos
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjetoForm

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
        "categorias": Categoria.objects.all(),
    }
    return render(request, "categoria.html",
                  contexto)

def novo_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect("/projetos/")
    else:
        form = ProjetoForm()
        return render(request, "novo_projeto.html",
                    {"form": form})

def detalhe_projeto(request, id):
    projeto = get_object_or_404(Projetos, id=id)
    return render(request, "detalhe_projeto.html", {"projeto": projeto})

def editar_projeto(request, id):
    projeto = get_object_or_404(Projetos, id=id)
    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect("/projetos/")
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, "novo_projeto.html", {"form": form})

def excluir_projeto(request, id):
    projeto = get_object_or_404(Projetos, id=id)
    if request.method == "POST":
        projeto.delete()
        return redirect("/projetos/")
    return render(request, "excluir_projeto.html", {"projeto": projeto})