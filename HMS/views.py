from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')

def user_login(request):
    return render(request, 'login.html')
def appointments(request):
    return render(request, 'appointments.html')
def settings(request):
    return render(request, 'settings.html')