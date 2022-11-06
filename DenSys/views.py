from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import DoctorForm,PatientForm,DoctorUpdateForm,UpdateUserForm,PatientUpdateForm
from .models import Doctor,Patient

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView

from .models import User
from django.db.models import Q




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
    Doctors = User.objects.filter(Q(is_doctor=True))
    Patients = User.objects.filter(Q(is_patient=True))

    context = {'Doctors': Doctors,'Patients': Patients}

    return render(request,'DenSys/main.html',context)


def doctor_page(request,pk):
    doctor = Doctor.objects.get(id=pk)
    context = {'doctor': doctor}
    return render(request,'DenSys/doctor.html',context)

###
class create_doctor(CreateView):
    model = User
    form_class = DoctorForm
    template_name = 'DenSys/doctor_form.html'

    context = {'form_class': form_class}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')
###
def update_doctor(request,pk):
    user2 = User.objects.get(id=pk)
    doctor = Doctor.objects.get(user=user2)
    form = DoctorUpdateForm(instance=doctor)
    user_form = UpdateUserForm(instance=user2)
    if request.method == 'POST':
        form = DoctorUpdateForm(request.POST, instance=doctor)
        user_form = UpdateUserForm(request.POST,instance=user2)
        if form.is_valid() and user_form.is_valid():
            user_form.save()
            form.save()
            return redirect('main')

    context = {'form': form, 'user_form': user_form}
    return render(request, 'DenSys/doctor_form.html', context)


def delete_doctor(request,pk):
    doctor = User.objects.get(id=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('main')
    return render(request,'DenSys/delete.html',{'obj' : doctor})


def patient_page(request,pk):
    patient = Patient.objects.get(id=pk)
    context = {'patient': patient}
    return render(request,'DenSys/patient.html',context)

###

class create_patient(CreateView):
    model = User
    form_class = PatientForm
    template_name = 'DenSys/patient_form.html'

    context = {'form_class': form_class}
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')
####

def update_patient(request,pk):
    user2 = User.objects.get(id=pk)
    patient = Patient.objects.get(user=user2)
    form = PatientUpdateForm(instance=patient)
    user_form = UpdateUserForm(instance=user2)
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=patient)
        user_form = UpdateUserForm(request.POST,instance=user2)
        if form.is_valid() and user_form.is_valid():
            user_form.save()
            form.save()
            return redirect('main')

    context = {'form': form, 'user_form': user_form}
    return render(request, 'DenSys/patient_form.html', context)




def delete_patient(request,pk):
    patient = User.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('main')
    return render(request,'DenSys/delete.html',{'obj' : patient})