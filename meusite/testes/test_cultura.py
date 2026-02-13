import pytest
from django.urls import reverse
from meusite.models import PontoHistorico

@pytest.mark.django_db
def test_cultura_aparece(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="teste",
        password="123456"
    )

    client.login(username="teste", password="123456")

    PontoHistorico.objects.create(
        titulo="Teste Cultura",
        descricao="Descrição teste",
        categoria="CULTURAS"
    )

    response = client.get(reverse("home"))

    assert "Teste Cultura" in response.content.decode()
