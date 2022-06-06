from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha', 'curso_selecionado')
    search_fields = ('nome', 'email', 'curso_selecionado')
    readonly_fields = ('senha',)




