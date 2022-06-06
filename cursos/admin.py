from django.contrib import admin
from .models import Cursos

@admin.register(Cursos)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome_curso', 'descricao')
    search_fields = ['nome_curso']


