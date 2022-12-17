from django.urls import path
from . import views
urlpatterns = [

    path('',views.loginPage,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('main/', views.main_page,name="main"),
    path('usermain/', views.usermain,name="usermain"),
    path('makeregistration/', views.makeregistration,name="makeregistration"),


    path('doctor/', views.doctor_page,name="doctorpage"),

    path('profile/',views.userpage,name="userpage"),

    path('create-doctor/',views.create_doctor.as_view(),name="create-doctor"),
    path('update-doctor/<str:pk>/',views.update_doctor,name="update-doctor"),
    path('delete-doctor/<str:pk>/',views.delete_doctor,name="delete-doctor"),

    path('patient/', views.patient_page,name="patient"),
    path('create-patient/',views.create_patient.as_view(),name="create-patient"),
    path('update-patient/<str:pk>/',views.update_patient,name="update-patient"),
    path('delete-patient/<str:pk>/',views.delete_patient,name="delete-patient"),



    path('create-schedule/<str:pk>/',views.createschedule,name="create-schedule"),
    path('update-schedule/<str:pk>/',views.updateschedule,name="update-schedule"),
    path('delete-schedule/<str:pk>/',views.deleteschedule,name="delete-schedule"),

    path('create-treatment/<str:pk>/',views.createtreatment,name="create-treatment"),
    path('update-treatment/<str:pk>/',views.updatetreatment,name="update-treatment"),
    path('delete-treatment/<str:pk>/',views.deletetreatment,name="delete-treatment"),




]