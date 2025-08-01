from django.contrib import admin

from .models import studentModel

class StudentAdmin(admin.ModelAdmin):
    list_display =['name', 'email',]

admin.site.register(studentModel, StudentAdmin)