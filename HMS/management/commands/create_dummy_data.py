# filepath: /Users/anthonyrozet/Documents/healthcare-management-system/HMS/management/commands/create_dummy_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from HMS.models import Patient, Appointment, Prescription
from datetime import date, time

class Command(BaseCommand):
    help = 'Create dummy data for testing'

    def handle(self, *args, **kwargs):
        # Create a dummy user
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.stdout.write(f"User created: {user.username}")

        # Create a corresponding profile
        profile = Patient.objects.create(
            user=user,
            age=30,
            gender='Male',
            phone_number='1234567890',
            emergency_contact_name='John Doe',
            emergency_contact_phone='0987654321',
            insurance_company='HealthCare Inc.',
            insurance_id='HC123456'
        )
        self.stdout.write(f"Profile created for: {profile.user.username}")

        # Create dummy appointments
        Appointment.objects.create(
            patient=profile,
            appointment_date=date(2025, 5, 20),
            reason='Follow-up appointment'
        )
        Appointment.objects.create(
            patient=profile,
            appointment_date=date(2025, 5, 25),
            reason='Routine check-up'
        )
        self.stdout.write("Dummy appointments created.")

        # Create dummy prescriptions
        Prescription.objects.create(
            patient=profile,
            medication_name='Paracetamol',
            dosage='500mg',
            date_issued=date(2025, 5, 1),
            refills=2
        )
        Prescription.objects.create(
            patient=profile,
            medication_name='Ibuprofen',
            dosage='200mg',
            date_issued=date(2025, 5, 1),
            refills=2
        )
        self.stdout.write("Dummy prescriptions created.")