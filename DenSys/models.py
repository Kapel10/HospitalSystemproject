from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django import forms
from django.forms import widgets

# Create your models here.

from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)



    IIN_number = models.PositiveIntegerField(default='0000000000')
    ID_number = models.PositiveIntegerField(null=True)

    contact_number = models.CharField(max_length=12,default='00000000')

    address = models.CharField(max_length=100,null=True)



    #id_number
    #contact_number
    #address
    is_patient = models.BooleanField('patient status', default=False)
    is_doctor = models.BooleanField('doctor status', default=False)


class Doctor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    department_id = [

        ('medicine', 'medicine'),
        ('surgery', 'surgery'),
        ('gynecology', 'gynecology'),
        ('obstetrics', 'obstetrics'),
        ('pediatrics', 'pediatrics'),
        ('radiology', 'radiology'),
        ('eye', 'eye'),
        ('dental', 'dental'),
        ('orthopedics', 'orthopedics'),
        ('neurology', 'neurology'),
        ('cardiology', 'cardiology'),
        ('psychiatry', 'psychiatry'),
        ('skin', 'skin'),



    ]
    department_id = models.CharField(max_length=100, choices=department_id, default='medicine')

    specialization_id = schedule_details = models.CharField(max_length=100,null=True)
    experience = models.PositiveIntegerField(null=True)

    price = models.PositiveIntegerField(null=True)

    category = [

        ('highest', 'highest'),
        ('first', 'first'),
        ('second', 'second'),
        ('middle', 'middle'),

    ]

    category = models.CharField(max_length=100, choices=category, default='second')

    ratings = models.PositiveIntegerField(null=True,validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])

    schedule_details = models.CharField(max_length=100,null=True)

    degree = [

        ('MD', 'MD'),
        ('PhD', 'PhD'),
        ('Bachelor', 'Bachelor'),
        ('Doctoral', 'Doctoral'),

    ]

    degree = models.CharField(max_length=100, choices=degree, default='Bachelor')

    image_doctor = models.ImageField(upload_to='media/static/img',null=True,default="")






    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.first_name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    emergency_contact_number = models.CharField(max_length=12,null=True)

    blood_group = [
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    blood_group = models.CharField(max_length=10, choices=blood_group, default='A+')


    marital_status = [

        ('married', 'married'),
        ('divorced', 'divorced'),
        ('never_married', 'never_married'),

    ]

    marital_status = models.CharField(max_length=100, choices=marital_status,default='never_married')











    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


class Schedule(models.Model):

    patient_schedule = models.CharField(max_length=100,null=True)
    doctor_schedule = models.CharField(max_length=100, null=True)

    status = [

        ('denied', 'denied'),
        ('approved', 'approved'),

    ]
    status = models.CharField(max_length=100, choices=status, default='denied',null=True)

    checked = [

        ('unseen', 'unseen'),
        ('seen', 'seen'),

    ]
    checked = models.CharField(max_length=100, choices=checked, default='unseen', null=True)

    date = models.DateField(null=True)
    time = models.TimeField(null=True)










    name = models.CharField(max_length=100,null=True)
    surname = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.id)



class Treatment(models.Model):
    doctor = models.CharField(max_length=100, null=True)
    patient_treatment = models.CharField(max_length=100, null=True)
    topic = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    first_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return str(self.topic)


