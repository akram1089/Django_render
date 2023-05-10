from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import StudentData
class StudentAdmin(admin.ModelAdmin):
    list_display=("name","email","roll_num","stream")

admin.site.register(StudentData,StudentAdmin)
