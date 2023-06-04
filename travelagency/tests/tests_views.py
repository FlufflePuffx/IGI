import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_view(client):
   url = reverse('home')
   guest_response = client.get(url)
   assert guest_response.status_code == 200


@pytest.mark.django_db
def test_not_error_view(client):
   url = reverse('home')
   guest_response = client.get(url)
   assert guest_response.status_code != 404


@pytest.mark.django_db
def test_user_view(client):
   url = reverse('home')
   user_response = client.get(url)
   assert user_response.status_code == 200


@pytest.mark.django_db
def test_not_error_user_view(client):
   url = reverse('home')
   user_response = client.get(url)
   assert user_response.status_code != 404

@pytest.mark.django_db
def test_reg_user_view(client):
   url = reverse('home')
   reg_user_response = client.get(url)
   assert reg_user_response.status_code == 200


@pytest.mark.django_db
def test_not_error_reg_user_view(client):
   url = reverse('home')
   reg_user_response = client.get(url)
   assert reg_user_response.status_code != 404


@pytest.mark.django_db
def test_admin_view(client):
   url = reverse('home')
   admin_response = client.get(url)
   assert admin_response.status_code == 200


@pytest.mark.django_db
def test_not_error_admin_view(client):
   url = reverse('home')
   admin_response = client.get(url)
   assert admin_response.status_code != 404
