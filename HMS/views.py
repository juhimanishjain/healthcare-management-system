from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request, 'homepage.html')

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
def appointments(request):
    return render(request, 'appointments.html')
def settings(request):
    return render(request, 'settings.html')