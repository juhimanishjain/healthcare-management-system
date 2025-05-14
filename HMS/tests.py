from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))  # Assuming 'home' is the name of your home URL
        self.assertEqual(response.status_code, 200)

class PrescriptionViewerTests(TestCase):
    def test_prescription_view_status_code(self):
        response = self.client.get(reverse('prescriptions'))  # Assuming 'prescriptions' is the name of your prescriptions URL
        self.assertEqual(response.status_code, 200)

class SettingsPageTests(TestCase):
    def test_settings_page_status_code(self):
        response = self.client.get(reverse('settings'))  # Assuming 'settings' is the name of your settings URL
        self.assertEqual(response.status_code, 200)