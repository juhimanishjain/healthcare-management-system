from django.db import models
from django.contrib.auth.models import User



class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    insurance_company = models.CharField(max_length=100, blank=True, null=True)
    insurance_id = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.user.username
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} on {self.appointment_date}"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    date_issued = models.DateField()
    refills = models.IntegerField()

    def __str__(self):
        return f"{self.medication_name} prescribed to {self.patient}"
    
class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    date_diagnosed = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.condition} ({self.date_diagnosed})"


class Surgery(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    procedure = models.CharField(max_length=255)
    date_performed = models.DateField()
    hospital = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.procedure} on {self.date_performed}"
    
class LabReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    date_conducted = models.DateField()
    result_summary = models.TextField(blank=True)
    uploaded_file = models.FileField(upload_to='lab_reports/', blank=True)

    def __str__(self):
        return f"{self.test_name} ({self.date_conducted})"

