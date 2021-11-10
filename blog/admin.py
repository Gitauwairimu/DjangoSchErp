from django.contrib import admin
from .models import Attendance, Friend, Student, Staff, School

# Register your models here.
admin.site.register(Friend)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Attendance)
admin.site.register(School)