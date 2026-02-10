from django.db import models


from django.db import models

class PontoHistorico(models.Model):
    CATEGORIAS = (
        ('Culturas', 'Culturas'),
        ('TRAJETORIA', 'Trajetória '),
        ('ROTEIRO', 'Roteiro Acessível (Idosos)'),
    )
    
    titulo = models.CharField(max_length=200, help_text="Ex: Soja ou As Raízes Indígenas")
    subtitulo = models.CharField(max_length=255, blank=True, null=True, help_text="Ex: O Gigante do Agronegócio")
    descricao = models.TextField(help_text="Conteúdo principal do texto")
    imagem = models.ImageField(upload_to='pontos_historicos/', blank=True, null=True)
    audio_guia = models.FileField(upload_to='audios/', blank=True, null=True)
    localizacao_url = models.URLField(max_length=500, blank=True, null=True, help_text="Link do Google Maps")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    ordem = models.IntegerField(default=0, help_text="Quanto menor o número, mais no topo aparece")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ponto Histórico/Cultural"
        ordering = ['ordem', 'titulo']

    def __str__(self):
        return f"[{self.get_categoria_display()}] {self.titulo}"