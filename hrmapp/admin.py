from django.contrib import admin
from .models import Department
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['dept_id','dept_name','description','created_at','updated_at','status']
admin.site.register(Department,DepartmentAdmin)