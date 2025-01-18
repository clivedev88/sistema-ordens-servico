from django.contrib import admin
from .models import OrdemServico

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'status', 'data_criacao')
    list_filter = ('status', 'data_criacao')
    search_fields = ('cliente', 'descricao')
