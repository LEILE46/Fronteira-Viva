from django.contrib import admin
from .models import PontoHistorico, HistoriaColaborativa, PerfilUsuario

@admin.register(HistoriaColaborativa)
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'aprovado', 'data_envio')
    list_filter = ('aprovado', 'data_envio')
    search_fields = ('titulo', 'conteudo', 'autor__username')
    actions = ['aprovar_historias', 'reprovar_historias']

    @admin.action(description="Aprovar histórias selecionadas")
    def aprovar_historias(self, request, queryset):
        queryset.update(aprovado=True)

    @admin.action(description="Reprovar/Ocultar histórias selecionadas")
    def reprovar_historias(self, request, queryset):
        queryset.update(aprovado=False)

@admin.register(PontoHistorico)
class PontoHistoricoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordem', 'titulo', 'categoria', 'data_cadastro')
    list_editable = ('ordem', 'categoria') 
    list_display_links = ('id', 'titulo') # Define quais campos abrem a edição
    list_filter = ('categoria',)
    search_fields = ('titulo', 'descricao')
    ordering = ('ordem',)

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'categoria', 'ordem')
        }),
        ('Mídia e Localização', {
            'fields': ('imagem', 'audio_guia', 'localizacao_url')
        }),
    )

@admin.register(PerfilUsuario)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'fonte_grande', 'alto_contraste')
    list_filter = ('fonte_grande', 'alto_contraste')
    search_fields = ('user__username', 'user__email')
