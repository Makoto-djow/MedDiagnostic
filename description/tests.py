from django.test import TestCase

from django.urls import reverse

from description.models import Doctors


# Тест для DoctorsListView
class DoctorsListViewTest(TestCase):
    def test_doctors_list_view(self):
        response = self.client.get(reverse('doctor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'description/doctors_list.html')


# Тест для DoctorsDetailView
class DoctorsDetailViewTest(TestCase):
    def setUp(self):
        self.doctor = Doctors.objects.create(name='Doctor Name', specialization='Specialization')

    def test_doctor_detail_view(self):
        url = reverse('doctor_detail', args=[self.doctor.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.doctor.name)
        self.assertQuerysetEqual(response.context['doctor'], ['<Doctors: Doctor Name>'])
