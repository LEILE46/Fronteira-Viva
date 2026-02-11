from django.contrib import admin
from .models import HistoriaColaborativa

@admin.register(HistoriaColaborativa)
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'aprovado', 'data_envio')
    list_filter = ('aprovado', 'data_envio')
    search_fields = ('titulo', 'conteudo', 'autor__username')
    actions = ['aprovar_historias']

    @admin.action(description="Aprovar histórias selecionadas")
    def aprovar_historias(self, request, queryset):
        queryset.update(aprovado=True)