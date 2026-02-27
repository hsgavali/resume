from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)

    def __str__(self):
        full_name = self.user.get_full_name()
        return full_name if full_name else self.user.username




class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default='Pending')


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    prescription = models.TextField()
    date = models.DateField(auto_now_add=True)


class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)


class LabReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=200)
    result = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.test_name} - {self.patient.name}"


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine)
    instructions = models.TextField()
    date = models.DateField(auto_now_add=True)
