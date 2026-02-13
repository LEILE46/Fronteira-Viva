import pytest
from django.urls import reverse
from meusite.models import PontoHistorico


@pytest.mark.django_db
def test_historia_cadastrada_aparece_na_pagina(client, django_user_model):

    # cria usuário
    user = django_user_model.objects.create_user(
        username="teste",
        password="123456"
    )

    # faz login
    client.login(username="teste", password="123456")

    # cria história
    PontoHistorico.objects.create(
        titulo="História Teste",
        descricao="Essa é uma história de teste.",
        categoria="HISTORIAS"
    )

    response = client.get(reverse("home"))

    content = response.content.decode()

    assert "História Teste" in content

