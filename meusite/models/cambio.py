from django.db import models

class Cambio(models.Model):
    MOEDAS = (
        ('USD', 'Dólar (US$)'),
        ('PYG', 'Guarani (₲)'),
    )
    moeda = models.CharField(max_length=3, choices=MOEDAS)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    casa_cambio = models.CharField(max_length=100)
    melhor_cotacao = models.BooleanField(default=False)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.moeda} - {self.casa_cambio} (R$ {self.valor})"

