import pytest
from django.urls import reverse
from meusite.models import PontoHistorico  # ajuste para o nome real do seu model

@pytest.mark.django_db
def test_historia_cadastrada_aparece_na_pagina(client):
    
    # Criando uma história como se tivesse sido cadastrada no admin
    PontoHistorico.objects.create(
        titulo="História Teste",
        descricao="Essa é uma história de teste.",
        categoria="HISTORIAS"
    )

    response = client.get(reverse("home"))

    content = response.content.decode()

    # Verifica se o título aparece
    assert "História Teste" in content
    
    # Verifica se a descrição aparece
    assert "Essa é uma história de teste." in content