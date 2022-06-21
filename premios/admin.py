from django.contrib import admin
from .models import Premio

@admin.register(Premio)
class PremioAdmin(admin.ModelAdmin):
    list_display = ('nome_premio', 'descricao')
    search_fields = ['nome_premio']


