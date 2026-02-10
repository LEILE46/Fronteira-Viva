from django.db import models
from django.contrib.auth.models import User

class HistoriaColaborativa(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)  # Regra de Negócio: Precisa de aprovação

    class Meta:
        verbose_name = "História dos Usuários"
        ordering = ['-data_envio']

    def __str__(self):
        return f"{self.titulo} - Enviado por: {self.autor.username}"