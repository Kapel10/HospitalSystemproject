from django.forms import ModelForm
from .models import Doctor,Patient, User
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

    birth_date = forms.DateTimeField(required=True)

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

        user.birth_date = self.cleaned_data.get('birth_date')

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

    birth_date = forms.DateTimeField(required=True)

    contact_number = forms.CharField(required=True)

    address = forms.CharField(required=True)

    department_id = forms.IntegerField(required=True)
    specialization_id = forms.IntegerField(required=True)
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

        user.birth_date = self.cleaned_data.get('birth_date')

        user.contact_number = self.cleaned_data.get('contact_number')

        user.address = self.cleaned_data.get('address')



        user.save()

        doctor = Doctor.objects.create(user=user)

        doctor.marital_status = self.cleaned_data.get('department_id')
        doctor.marital_status = self.cleaned_data.get('specialization_id')
        doctor.marital_status = self.cleaned_data.get('experience')
        doctor.marital_status = self.cleaned_data.get('price')

        doctor.marital_status = self.cleaned_data.get('category')
        doctor.marital_status = self.cleaned_data.get('degree')

        doctor.marital_status = self.cleaned_data.get('ratings')
        doctor.marital_status = self.cleaned_data.get('schedule_details')


        doctor.save()
        return user

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    birth_date = forms.DateTimeField(required=True)

    IIN_number = forms.IntegerField(required=True)
    ID_number = forms.IntegerField(required=True)

    contact_number = forms.IntegerField(required=True)

    address = forms.CharField(required=True)




    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "middle_name", "birth_date", "IIN_number", "ID_number", "contact_number","address")


class DoctorUpdateForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ("department_id", "specialization_id", "experience", "price", "category", "degree", "ratings", "schedule_details" )


class PatientUpdateForm(ModelForm):
    class Meta:
        model = Patient
        fields = ("emergency_contact_number", "blood_group", "marital_status")
