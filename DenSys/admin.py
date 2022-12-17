from django.contrib import admin
from  .models import Doctor,Patient,User,Schedule,Treatment
# Register your models here.

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Schedule)
admin.site.register(Treatment)