from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))  # Assuming 'home' is the name of your home URL
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_context(self):
        response = self.client.get(reverse('home'))
        self.assertIn('recent_transactions', response.context)

class PrescriptionViewerTests(TestCase):
    def test_prescription_view_status_code(self):
        response = self.client.get(reverse('prescriptions'))  # Assuming 'prescriptions' is the name of your prescriptions URL
        self.assertEqual(response.status_code, 200)

    def test_prescription_view_template(self):
        response = self.client.get(reverse('prescriptions'))
        self.assertTemplateUsed(response, 'prescriptions.html')

    def test_prescription_view_context(self):
        response = self.client.get(reverse('prescriptions'))
        self.assertIn('prescriptions', response.context)


class SettingsPageTests(TestCase):
    def test_settings_page_status_code(self):
        response = self.client.get(reverse('settings'))  
        self.assertEqual(response.status_code, 200)

    def test_settings_page_template(self):
        response = self.client.get(reverse('settings'))
        self.assertTemplateUsed(response, 'settings.html')

    def test_settings_page_context(self):
        response = self.client.get(reverse('settings'))
        self.assertIn('user_preferences', response.context)

class AuthenticatedHomePageTests(TestCase):
    def test_redirect_for_unauthenticated_user(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/login/?next=/')

    def test_home_page_for_authenticated_user(self):
        user = self.create_user()  
        self.client.login(username=user.username, password='password')  
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        

