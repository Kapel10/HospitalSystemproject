from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import DoctorForm,PatientForm,DoctorUpdateForm,UpdateUserForm,PatientUpdateForm,ScheduleForm,ScheduleuserForm,TreatmentForm
from .models import Doctor,Patient,Schedule,Treatment

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView

from .models import User
from django.db.models import Q
from django import forms




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
            if user.is_patient:

                return redirect('usermain')
            elif user.is_doctor:
                return redirect('doctorpage')
            else:
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
    schedule = Schedule.objects.all()
    checked = Schedule.objects.all().filter(checked='seen')
    unchecked = Schedule.objects.all().filter(checked='unseen')

    treat = Treatment.objects.all()

    context = {'Doctors': Doctors,'Patients': Patients, 'schedule':schedule,'checked':checked,'unchecked':unchecked,'treat':treat}

    return render(request,'DenSys/main.html',context)

def usermain(request):
    return render(request,'DenSys/usermain.html')

def makeregistration(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    #doctor = Doctor.objects.all()
    schedule = Schedule.objects.all()
    doctors_names = Doctor.objects.all().filter(Q(specialization_id__contains=q) |
                                                Q(user__first_name__contains=q) |
                                                Q(department_id__contains=q)
                                                )

    doctors_special = Doctor.objects.all().values('specialization_id').distinct()

    doctor_medicine = Doctor.objects.all().filter(department_id='medicine')
    doctor_surgery = Doctor.objects.all().filter(department_id='surgery')
    doctor_gynecology = Doctor.objects.all().filter(department_id='gynecology')
    doctor_obstetrics = Doctor.objects.all().filter(department_id='obstetrics')
    doctor_pediatrics = Doctor.objects.all().filter(department_id='pediatrics')
    doctor_radiology = Doctor.objects.all().filter(department_id='radiology')
    doctor_eye = Doctor.objects.all().filter(department_id='eye')
    doctor_dental = Doctor.objects.all().filter(department_id='dental')
    doctor_orthopedics = Doctor.objects.all().filter(department_id='orthopedics')
    doctor_neurology = Doctor.objects.all().filter(department_id='neurology')
    doctor_cardiology = Doctor.objects.all().filter(department_id='cardiology')
    doctor_psychiatry = Doctor.objects.all().filter(department_id='psychiatry')
    doctor_skin = Doctor.objects.all().filter(department_id='skin')

    all_doctors = Doctor.objects.all().values('department_id').distinct()






    context = {'schedule':schedule,'doctor_names':doctors_names,'doctor_special':doctors_special,'doctor_medicine':doctor_medicine,'doctor_surgery':doctor_surgery,'doctor_gynecology':doctor_gynecology,'doctor_obstetrics':doctor_obstetrics,'doctor_pediatrics':doctor_pediatrics, 'doctor_radiology':doctor_radiology, 'doctor_eye':doctor_eye,
               'doctor_dental':doctor_dental,'doctor_orthopedics':doctor_orthopedics,'doctor_neurology':doctor_neurology,
               'doctor_cardiology':doctor_cardiology,'doctor_psychiatry':doctor_psychiatry,'doctor_skin':doctor_skin,'all_doctors':all_doctors}

    return render(request, 'DenSys/appoint.html', context)

def userpage(request):
    user2 = User.objects.get(first_name=request.user.first_name)
    patient = Patient.objects.get(user=user2)
    sched = Schedule.objects.all().filter(patient_schedule=patient,status='approved')

    treatments = Treatment.objects.all().filter(patient_treatment=patient)
    context = {'patient': patient,'sched':sched,'treatments':treatments}
    return render(request,'DenSys/userpage.html',context)



def doctor_page(request):
    user2 = User.objects.get(first_name=request.user.first_name)
    doctor = Doctor.objects.get(user=user2)
    treat = Treatment.objects.all()

    treat_special = Treatment.objects.all().filter(doctor=doctor)
    schedule = Schedule.objects.all().filter(doctor_schedule=request.user.first_name,status='approved')





    context = {'doctor': doctor,'schedule':schedule,'treat':treat,'treat_special':treat_special}

    return render(request,'DenSys/doctorpage.html',context)

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
        form = DoctorUpdateForm(request.POST,request.FILES, instance=doctor)
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


####################################################################v##########################################################################################################################################################################

def createschedule(request,pk):
    user2 = User.objects.get(id=pk)
    my_doctor = Doctor.objects.get(user=user2)
    form = ScheduleuserForm(initial={'patient_schedule' : request.user.first_name,'doctor_schedule' : my_doctor})
    if request.method == 'POST':
        form = ScheduleuserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('makeregistration')
    context = {'form': form}
    return render(request, 'DenSys/schedule_user.html', context)


def updateschedule(request,pk):
    schedule = Schedule.objects.get(id=pk)
    form = ScheduleForm(instance=schedule)
    if request.method == 'POST':
        form = ScheduleForm(request.POST,instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {'form' : form}
    return render(request,'DenSys/schedule_form.html',context)


def deleteschedule(request,pk):
    schedule = Schedule.objects.get(id=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('main')
    context = {'obj': schedule}
    return render(request,'DenSys/delete.html',context)

####################################################################v##########################################################################################################################################################################

def createtreatment(request,pk):
    user2 = User.objects.get(first_name=pk)
    patient = Patient.objects.get(user=user2)
    form = TreatmentForm(initial={'patient_treatment' : patient,'doctor': request.user.first_name})
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctorpage')
    context = {'form': form}
    return render(request, 'DenSys/treatment_form.html', context)


def updatetreatment(request,pk):
    treatment = Treatment.objects.get(id=pk)
    form = TreatmentForm(instance=treatment)
    if request.method == 'POST':
        form = TreatmentForm(request.POST,instance=treatment)
        if form.is_valid():
            form.save()
            return redirect('doctorpage')
    context = {'form' : form}
    return render(request,'DenSys/treatment_form.html',context)


def deletetreatment(request,pk):
    treatment = Treatment.objects.get(id=pk)
    if request.method == 'POST':
        treatment.delete()
        return redirect('doctorpage')
    context = {'obj': treatment}
    return render(request,'DenSys/delete.html',context)