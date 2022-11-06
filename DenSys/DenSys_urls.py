from django.urls import path
from . import views
urlpatterns = [

    path('',views.loginPage,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('main/', views.main_page,name="main"),
    path('doctor/<str:pk>/', views.doctor_page,name="doctor"),
    path('create-doctor/',views.create_doctor.as_view(),name="create-doctor"),
    path('update-doctor/<str:pk>/',views.update_doctor,name="update-doctor"),
    path('delete-doctor/<str:pk>/',views.delete_doctor,name="delete-doctor"),

    path('patient/', views.patient_page,name="patient"),
    path('create-patient/',views.create_patient.as_view(),name="create-patient"),
    path('update-patient/<str:pk>/',views.update_patient,name="update-patient"),
    path('delete-patient/<str:pk>/',views.delete_patient,name="delete-patient"),


]