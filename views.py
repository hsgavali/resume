from django.shortcuts import render
from .models import (
    Doctor,
    Patient,
    Appointment,
    Bill,
    LabReport,
    Medicine
)

def index(request):
    doctor_count = Doctor.objects.count()
    patient_count = Patient.objects.count()
    appointment_count = Appointment.objects.count()
    recent_appointments = Appointment.objects.all().order_by('-date')[:5]

    context = {
        'doctor_count': doctor_count,
        'patient_count': patient_count,
        'appointment_count': appointment_count,
        'recent_appointments': recent_appointments,
    }
    return render(request, 'hms/index.html', context)


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hms/patients/list.html', {'patients': patients})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hms/appointments/list.html', {'appointments': appointments})


def lab_reports(request):
    reports = LabReport.objects.all()
    return render(request, 'hms/lab_reports.html', {'reports': reports})


def pharmacy(request):
    medicines = Medicine.objects.all()
    return render(request, 'hms/pharmacy.html', {'medicines': medicines})
