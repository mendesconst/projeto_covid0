from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'token_cadastro', 'senha', 'curso_selecionado')
    search_fields = ('nome', 'token_cadastro', 'curso_selecionado')
    readonly_fields = ('senha',)




