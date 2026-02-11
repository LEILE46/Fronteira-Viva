import pytest
from django.urls import reverse
from meusite.models import PontoHistorico

@pytest.mark.django_db
def test_cultura_aparece(client):
    PontoHistorico.objects.create(
        titulo="Teste Cultura",
        descricao="Descrição teste",
        categoria="CULTURAS"
    )

    response = client.get(reverse("home"))

    assert "Teste Cultura" in response.content.decode()