from django.forms import ModelForm
from .models import Doctor,Patient, User, Schedule,Treatment
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.forms import widgets


class PatientForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    IIN_number = forms.IntegerField(required=True)
    ID_number = forms.IntegerField(required=True)



    contact_number = forms.CharField(required=True)
    emergency_contact_number = forms.CharField(required=True)



    address = forms.CharField(required=True)


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


    blood_group = forms.ChoiceField(choices=blood_group)

    marital_status = [

        ('married', 'married'),
        ('divorced', 'divorced'),
        ('never_married', 'never_married'),

    ]
    marital_status = forms.ChoiceField(choices=marital_status)


    class Meta(UserCreationForm.Meta):
        model = User





    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()

        user.first_name = self.cleaned_data.get('first_name')
        user.middle_name = self.cleaned_data.get('middle_name')
        user.last_name = self.cleaned_data.get('last_name')

        user.IIN_number = self.cleaned_data.get('IIN_number')
        user.ID_number = self.cleaned_data.get('ID_number')



        user.contact_number = self.cleaned_data.get('contact_number')


        user.address = self.cleaned_data.get('address')

        user.save()

        patient = Patient.objects.create(user=user)

        patient.emergency_contact_number = self.cleaned_data.get('emergency_contact_number')

        patient.blood_group = self.cleaned_data.get('blood_group')

        patient.marital_status = self.cleaned_data.get('marital_status')





        patient.save()
        return user


class DoctorForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    IIN_number = forms.IntegerField(required=True)
    ID_number = forms.IntegerField(required=True)



    contact_number = forms.CharField(required=True)

    address = forms.CharField(required=True)
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
    department_id = forms.ChoiceField(choices=department_id)
    specialization_id = forms.CharField(required=True)
    experience = forms.IntegerField(required=True)
    price = forms.IntegerField(required=True)

    category = [

        ('highest', 'highest'),
        ('first', 'first'),
        ('second', 'second'),
        ('middle', 'middle'),

    ]

    category = forms.ChoiceField(choices=category)

    degree = [

        ('MD', 'MD'),
        ('PhD', 'PhD'),
        ('Bachelor', 'Bachelor'),
        ('Doctoral', 'Doctoral'),

    ]

    degree = forms.ChoiceField(choices=degree)

    ratings = forms.IntegerField(required=True)

    schedule_details = forms.CharField(required=True)

    image_doctor = forms.ImageField()



    class Meta(UserCreationForm.Meta):
        model = User
        #fields = '__all__'


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.is_staff = True
        user.save()
        user.first_name = self.cleaned_data.get('first_name')
        user.middle_name = self.cleaned_data.get('middle_name')
        user.last_name = self.cleaned_data.get('last_name')

        user.IIN_number = self.cleaned_data.get('IIN_number')
        user.ID_number = self.cleaned_data.get('ID_number')



        user.contact_number = self.cleaned_data.get('contact_number')

        user.address = self.cleaned_data.get('address')



        user.save()

        doctor = Doctor.objects.create(user=user)

        doctor.department_id = self.cleaned_data.get('department_id')
        doctor.specialization_id = self.cleaned_data.get('specialization_id')
        doctor.experience = self.cleaned_data.get('experience')
        doctor.price = self.cleaned_data.get('price')

        doctor.category = self.cleaned_data.get('category')
        doctor.degree = self.cleaned_data.get('degree')

        doctor.ratings = self.cleaned_data.get('ratings')
        doctor.schedule_details = self.cleaned_data.get('schedule_details')

        doctor.image_doctor = self.cleaned_data.get('image_doctor')


        doctor.save()
        return user

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))



    IIN_number = forms.IntegerField(required=True)
    ID_number = forms.IntegerField(required=True)

    contact_number = forms.IntegerField(required=True)

    address = forms.CharField(required=True)




    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "middle_name",  "IIN_number", "ID_number", "contact_number","address")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'input', 'required': True}),
            'first_name': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'middle_name': forms.TextInput(attrs={'class': 'input', 'required': True}),


            'IIN_number': forms.NumberInput(attrs={'class': 'input', 'required': True}),
            'ID_number': forms.NumberInput(attrs={'class': 'input', 'required': True}),
            'contact_number': forms.NumberInput(attrs={'class': 'input', 'required': True}),
            'address': forms.TextInput(attrs={'class': 'input', 'required': True}),
        }


class DoctorUpdateForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ("department_id", "specialization_id", "experience", "price", "category", "degree", "ratings", "schedule_details", "image_doctor" )
        widgets = {
            'department_id': forms.Select(attrs={'class': 'form-control', 'autofocus': True}),
            'specialization_id': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'experience': forms.NumberInput(attrs={'class': 'form-control', 'autofocus': True}),
            'price': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'category': forms.Select(attrs={'class': 'form-control', 'autofocus': True}),
            'degree': forms.Select(attrs={'class': 'input', 'required': True}),
            'ratings': forms.NumberInput(attrs={'class': 'form-control', 'autofocus': True}),
            'schedule_details': forms.TextInput(attrs={'class': 'input', 'required': True}),
            #'image_doctor': forms.FileInput(attrs={'class': 'input', 'required': True}),
        }

class PatientUpdateForm(ModelForm):
    class Meta:
        model = Patient
        fields = ("emergency_contact_number", "blood_group", "marital_status")
        widgets = {
            'emergency_contact_number': forms.NumberInput(attrs={'class': 'form-control', 'autofocus': True}),
            'blood_group': forms.Select(attrs={'class': 'input', 'required': True}),
            'marital_status': forms.Select(attrs={'class': 'form-control', 'autofocus': True}),

        }



class ScheduleForm(ModelForm):

    class Meta:
        model = Schedule
        fields = ("patient_schedule","doctor_schedule","status","name","surname","contact","checked","date","time")
        status = [

            ('denied', 'denied'),
            ('approved', 'divorced'),

        ]
        checked = [

            ('unseen', 'unseen'),
            ('seen', 'seen'),

        ]
        time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        widgets = {
            'patient_schedule': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'doctor_schedule': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'name': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'surname': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'contact': forms.TextInput(attrs={'class': 'input', 'required': True}),

            'date': forms.DateInput(attrs={'class': 'input', 'required': True}),




            'status': forms.Select(attrs={'class': 'input', 'required': False}),
            'checked': forms.Select(attrs={'class': 'input', 'required': False}),
        }


class ScheduleuserForm(ModelForm):


    class Meta:
        model = Schedule
        fields = ("name","surname","contact","doctor_schedule","patient_schedule","date","time")

        time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        widgets = {
            #'patient_schedule': forms.Select(attrs={'class': 'input', 'autofocus': True}),
            'doctor_schedule': forms.TextInput(attrs={'class': 'input', 'required': False,'type': 'hidden'}),
            'patient_schedule': forms.TextInput(attrs={'class': 'input', 'required': False,'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'surname': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'contact': forms.TextInput(attrs={'class': 'input', 'required': True}),

            'date': forms.DateInput(attrs={'class': 'input', 'required': True}),



        }



class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = ("doctor","patient_treatment","topic","description","first_date","end_date")
        widgets = {
            'doctor': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'patient_treatment': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'topic': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'description': forms.TextInput(attrs={'class': 'input', 'required': True}),

            'first_date': forms.DateInput(attrs={'class': 'input', 'required': True}),
            'end_date': forms.DateInput(attrs={'class': 'input', 'required': True}),


        }