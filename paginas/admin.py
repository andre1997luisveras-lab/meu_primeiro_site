from django.contrib import admin

# Register your models here.

from .models import Livros
admin.site.register(Livros)


from .models import Projetos
admin.site.register(Projetos)