from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.appointments, name='appointments'),
    path('prescriptions/', views.prescriptions_viewer, name='prescriptions_viewer'),
    path('settings/', views.settings, name='settings'),
    path('login/', views.user_login, name='login'),

]