from django.contrib import admin
from .models import District,Student,Teacher



admin.site.register(District)
# admin.site.register(Student)
admin.site.register(Teacher)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstname','mobile_no','education','email']
    list_filter = ['district']