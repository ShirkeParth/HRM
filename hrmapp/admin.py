from django.contrib import admin
from .models import Department,Role,Employee
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['dept_id','dept_name','description','created_at','updated_at','status']
admin.site.register(Department,DepartmentAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display=['role_name','description','created_at','updated_at','status']
admin.site.register(Role,RoleAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email', 'mobile', 'dept', 'role','reporting_manager', 'date_of_joining','status' ]
admin.site.register(Employee, EmployeeAdmin)