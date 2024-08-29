from django.test import TestCase
from users.models import User
from .views import ServicesListView, ServicesDetailView, ServicesCreateView, ServicesUpdateView, ServicesDeleteView


class ServicesListViewTest(TestCase):
    def test_services_list_view(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)


class ServicesDetailViewTest(TestCase):
    def test_services_detail_view(self):
        response = self.client.get('/services/1/')
        self.assertEqual(response.status_code, 200)


class ServicesCreateViewTest(TestCase):
    def test_services_create_view(self):
        data = {'service_name': 'New Service', 'description': 'A new service description'}
        response = self.client.post('/services/create/', data)
        self.assertEqual(response.status_code, 302)


class ServicesUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client.force_login(user=self.user)

    def test_services_update_view(self):
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='<PASSWORD>')
        response = self.client.get('/services/1/update/')
        self.assertEqual(response.status_code, 200)


class ServicesDeleteViewTest(TestCase):
    def test_services_delete_view(self):
        response = self.client.get('/services/1/delete/')
        self.assertEqual(response.status_code, 405)

        response = self.client.post('/services/1/delete/', data={})
        self.assertEqual(response.status_code, 302)