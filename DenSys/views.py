from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import DoctorForm,PatientForm
from .models import Doctor,Patient
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            messages.error(request, 'User name or password does not exist')
    context = {}
    return render(request,'DenSys/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def main_page(request):
    Doctors = Doctor.objects.all()
    Patients = Patient.objects.all()
    context = {'Doctors': Doctors,'Patients': Patients}
    return render(request,'DenSys/main.html',context)

@login_required(login_url='login')
def doctor_page(request,pk):
    doctor = Doctor.objects.get(id=pk)
    context = {'doctor': doctor}
    return render(request,'DenSys/doctor.html',context)
@login_required(login_url='login')
def create_doctor(request):
    form = DoctorForm
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')


    context ={'form': form}
    return render(request,'DenSys/doctor_form.html',context)

@login_required(login_url='login')
def update_doctor(request,pk):
    doctor = Doctor.objects.get(id=pk)
    form = DoctorForm(instance=doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('main')

    context = {'form': form}
    return render(request, 'DenSys/doctor_form.html', context)

@login_required(login_url='login')
def delete_doctor(request,pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('main')
    return render(request,'DenSys/delete.html',{'obj' : doctor})

@login_required(login_url='login')
def patient_page(request,pk):
    patient = Patient.objects.get(id=pk)
    context = {'patient': patient}
    return render(request,'DenSys/patient.html',context)


@login_required(login_url='login')
def create_patient(request):
    form = PatientForm
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context ={'form': form}
    return render(request,'DenSys/patient_form.html',context)

@login_required(login_url='login')
def update_patient(request,pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('main')

    context = {'form': form}
    return render(request, 'DenSys/patient_form.html', context)



@login_required(login_url='login')
def delete_patient(request,pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('main')
    return render(request,'DenSys/delete.html',{'obj' : patient})