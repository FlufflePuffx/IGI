import pytest

from django.contrib.auth.models import User
from tours.models import *


@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1


@pytest.mark.django_db
def test_tour_create():
  Tour.objects.create(title='test', description='some information', cost=199)
  assert Tour.objects.count() == 1


@pytest.mark.django_db
def test_tour_create_empty():
  Tour.objects.create()
  assert Tour.objects.count() == 1


@pytest.mark.django_db
def test_tour_create_title_only():
  Tour.objects.create(title='test')
  assert Tour.objects.count() == 1


@pytest.mark.django_db
def test_tour_create_cost_only():
  Tour.objects.create(cost=1599)
  assert Tour.objects.count() == 1


@pytest.mark.django_db
def test_tour_create_description_only():
  Tour.objects.create(description='just a tour')
  assert Tour.objects.count() == 1


@pytest.mark.django_db
def test_country_create():
  Country.objects.create(name='France', weather='15 deg')
  assert Country.objects.count() == 1


@pytest.mark.django_db
def test_country_name_only_create():
  Country.objects.create(name='Italy')
  assert Country.objects.count() == 1


@pytest.mark.django_db
def test_country_weather_only_create():
  Country.objects.create(weather='34 deg')
  assert Country.objects.count() == 1


@pytest.mark.django_db
def test_client_create():
  Client.objects.create(name='Jerry', tel_number='+375 29 201 48 74')
  assert Client.objects.count() == 1


@pytest.mark.django_db
def test_client_name_only_create():
  Client.objects.create(name='Hanna')
  assert Client.objects.count() == 1


@pytest.mark.django_db
def test_client_tel_number_only_create():
  Client.objects.create(tel_number='+375 44 742 36 01')
  assert Client.objects.count() == 1


@pytest.mark.django_db
def test_category_create():
  Category.objects.create(name='test category', slugify_name='test-category')
  assert Category.objects.count() == 1


@pytest.mark.django_db
def test_category_empty_create():
  Category.objects.create()
  assert Category.objects.count() == 1


@pytest.mark.django_db
def test_ticket_create():
  Ticket.objects.create()
  assert Ticket.objects.count() == 1


@pytest.mark.django_db
def test_term_create():
  Term.objects.create(days=14)
  assert Term.objects.count() == 1


@pytest.mark.django_db
def test_term_empty_create():
  Term.objects.create()
  assert Term.objects.count() == 1
