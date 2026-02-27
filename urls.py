from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.patient_list, name='patient_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('lab/', views.lab_reports, name='lab_reports'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
]
