import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_status_code(client):
    url = reverse('home')  # nome da sua url
    response = client.get(url)

    assert response.status_code == 200