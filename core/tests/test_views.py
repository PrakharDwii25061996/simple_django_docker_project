import pytest

from django.urls import reverse
from django.test import Client

from core.models import User


@pytest.fixture
def client():
	return Client()


@pytest.mark.django_db
class TestRegistrationView:

	def test_model_registration_successful_status(self, client):
		response = client.post(reverse('register'), {
			'name': 'Prakhar Dwivedi',
			'email': 'prak@gmail.com',
			'password': 'Mydime1233445'
		})
		assert response.status_code == 302
		assert User.objects.filter(email='prak@gmail.com').exists()

	def test_registration_with_mobile_number(self, client):
		response = client.post(reverse('register'), {
			'name': 'Prakhar Dwivedi',
			'email': 'prak2@gmail.com',
			'password': 'Mydime1233445',
			'mobile_number': '6260336626'
		})
		assert response.status_code == 302
		assert User.objects.filter(email='prak2@gmail.com').exists()

	def test_registration_view_check_valid_name(self, client):
		response = client.post(reverse('register'), {
			'email': 'prak3@gmail.com',
			'name': 'Anil Kapoor',
			'password': 'My4844848dj',
			'mobile_number': '6260336626'
		})
		assert response.status_code == 302
		assert User.objects.filter(name='Anil Kapoor').exists()


@pytest.fixture
def create_user():
	user = User.objects.create_user(
		email='prak22@gmail.com',
		user='Ansh Kapoor',
		password='Maadiue348383'
	)
	return user


@pytest.mark.django_db
class TestLoginView:

	def test_successfull_login(self, client, create_user):
		# user = create_user()
		response = client.post(reverse('register'), {
			'email': 'prak@gmail.com',
			'password': 'Mydime1233445'
		})
		assert response.status_code == 302
		assert User.objects.count() == 2


