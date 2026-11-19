from django.contrib import admin

# Register your models here.

from .models import Livros
from .models import Projetos
from .models import Categoria, Projetos

admin.site.register(Livros)
admin.site.register(Categoria)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano", "categoria")
    list_filter = ("categoria",)
    search_fields = ("nome", "descricao" )

admin.site.register(Projetos, ProjetoAdmin)



