from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    #  user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    IIN_number = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=12)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Patient(models.Model):
    #date_of_birth = models.DateTimeField()
    # user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    IIN_number = models.PositiveIntegerField()
    #ID_numbeer = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    #blood_group = (
    #   ('type', 'AB+'),
    #   ('type', 'AB-'),
    #   ('type', 'A+'),
    #   ('type', 'A-'),
    #   ('type', 'B+'),
    #    ('type', 'B-'),
    #   ('type', 'O+'),
    #    ('type', 'O-'),
    #    )

    #    contact_number = models.CharField(max_length=12)
    #   emergency_contact_number = models.CharField(max_length=12)
    #   address = models.CharField(max_length=30)








    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

