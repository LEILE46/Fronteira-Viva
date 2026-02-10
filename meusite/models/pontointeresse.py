from django.db import models


class PontoHistorico(models.Model):
    CATEGORIAS = (
        ('HISTORIA', 'História Local'),
        ('CULTURA', 'Cultura e Tradição'),
        ('ROTEIRO', 'Roteiro Acessível (Idosos)'),
    )
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='pontos_historicos/')
    audio_guia = models.FileField(upload_to='audios/', blank=True, null=True)
    localizacao_url = models.URLField(max_length=500, help_text="Link do Google Maps")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo