from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    fonte_grande = models.BooleanField(default=False)
    alto_contraste = models.BooleanField(default=False)