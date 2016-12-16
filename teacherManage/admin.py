from django.contrib import admin

# Register your models here.
from teacherManage.models import *


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(VIP)
admin.site.register(Appointment)

