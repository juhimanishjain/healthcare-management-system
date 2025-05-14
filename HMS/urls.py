from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.appointments, name='appointments'),
    path('prescriptions/', views.prescriptions_viewer, name='prescriptions_viewer'),
    path('settings/', views.settings, name='settings'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('past-medications/', views.past_medications_view, name='past_medications'),
    path('past-diagnosis/', views.past_diagnoses_view, name='past-diagnosis'),
    path('past-surgeries/', views.past_surgeries_view, name='past-surgeries'),
    path('lab-reports/', views.lab_reports_view, name='lab_reports'),
]