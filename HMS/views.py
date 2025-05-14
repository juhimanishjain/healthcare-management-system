from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Patient, Appointment, Prescription, Surgery, Diagnosis, LabReport

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # Create user
        user = User.objects.create_user(username=username, password=password)

        # Get extra patient info from form
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        emergency_name = request.POST.get('emergency_contact_name')
        emergency_phone = request.POST.get('emergency_contact_phone')
        insurance_company = request.POST.get('insurance_company')
        insurance_id = request.POST.get('insurance_id')

        # Create patient profile
        Patient.objects.create(
            user=user,
            age=age or None,
            gender=gender or None,
            phone_number=phone_number or None,
            emergency_contact_name=emergency_name or None,
            emergency_contact_phone=emergency_phone or None,
            insurance_company=insurance_company or None,
            insurance_id=insurance_id or None
        )

        messages.success(request, "Signup successful! You can now log in.")
        return redirect('login')

    return render(request, 'signup.html')

@login_required
def home(request):
    profile = Patient.objects.get(user=request.user)

    # Fetch upcoming appointments
    appointments = Appointment.objects.filter(patient=profile).order_by('appointment_date')

    # Fetch prescriptions (if needed)
    prescriptions = Prescription.objects.filter(patient=profile)

    context = {
        'profile': profile,
        'appointments': appointments,
        'prescriptions': prescriptions,
    }
    return render(request, 'homepage.html', context)
# Example view for the prescriptions viewer
def prescriptions_viewer(request):
    return render(request, 'prescriptions-viewer.html')

# Example view for the settings page


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def appointments(request):
    patient = Patient.objects.get(user=request.user)

    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason', 'General Consultation')  # optional

        
        from datetime import datetime
        appointment_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

        Appointment.objects.create(
            patient=patient,
            appointment_date=appointment_datetime,
            reason=reason
        )
        return redirect('home')  

    return render(request, 'appointments.html')  

@login_required
def settings(request):
    user = request.user
    profile = Patient.objects.get(user=user)

    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.dob = request.POST.get('dob')
        profile.gender = request.POST.get('gender')
        profile.phone_number = request.POST.get('phone_number')
        profile.emergency_contact_name = request.POST.get('emergency_contact_name')
        profile.emergency_contact_phone = request.POST.get('emergency_contact_phone')
        profile.save()

        email = request.POST.get('email')
        if email:
            user.email = email
            user.save()

        # Password change
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 and password1 == password2:
            user.set_password(password1)
            user.save()
            login(request, user)  

        if request.POST.get('deactivate') == 'true':
            user.is_active = False
            user.save()
            return redirect('login')

        return redirect('settings')  

    return render(request, 'settings.html', {'profile': profile})


@login_required
def past_medications_view(request):
    try:
        profile = Patient.objects.get(user=request.user)
        prescriptions = Prescription.objects.filter(patient=profile).order_by('-date_issued')
    except Patient.DoesNotExist:
        prescriptions = []

    return render(request, 'past-medications.html', {
        'prescriptions': prescriptions
    })

@login_required
def past_diagnoses_view(request):
    try:
        profile = Patient.objects.get(user=request.user)
        diagnoses = Diagnosis.objects.filter(patient=profile).order_by('-date_diagnosed')
    except Patient.DoesNotExist:
        diagnoses = []

    return render(request, 'past-diagnosis.html', {'diagnoses': diagnoses})


@login_required
def past_surgeries_view(request):
    try:
        profile = Patient.objects.get(user=request.user)
        surgeries = Surgery.objects.filter(patient=profile).order_by('-date_performed')
    except Patient.DoesNotExist:
        surgeries = []

    return render(request, 'past-surgeries.html', {'surgeries': surgeries})

@login_required
def lab_reports_view(request):
    patient = Patient.objects.get(user=request.user)
    reports = LabReport.objects.filter(patient=patient).order_by('-date_conducted')
    return render(request, 'lab_reports.html', {'reports': reports})

