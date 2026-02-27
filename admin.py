from django.contrib import admin
from .models import Doctor, Patient, Appointment, MedicalRecord, Bill, LabReport, Medicine, Prescription

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'availability')
    search_fields = ('user__username', 'specialization')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'contact')
    search_fields = ('name', 'contact')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'status')
    list_filter = ('status', 'date')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date')

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('patient', 'amount', 'date', 'paid')
    list_filter = ('paid', 'date')

@admin.register(LabReport)
class LabReportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_name', 'date')

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date')
