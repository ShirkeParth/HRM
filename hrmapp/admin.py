from django.contrib import admin
from .models import (
    Department,
    Role,
    Employee,
    OTP,
    Task,
    TaskAssignment
)

# ---------------- DEPARTMENT ----------------

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'dept_id',
        'dept_name',
        'description',
        'created_at',
        'updated_at',
        'status'
    ]

    search_fields = ['dept_name']
    list_filter = ['status']


# ---------------- ROLE ----------------

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'role_name',
        'description',
        'created_at',
        'updated_at',
        'status'
    ]

    search_fields = ['role_name']
    list_filter = ['status']


# ---------------- EMPLOYEE ----------------

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'mobile',
        'dept',
        'role',
        'reporting_manager',
        'date_of_joining',
        'status'
    ]

    search_fields = [
        'first_name',
        'last_name',
        'email'
    ]

    list_filter = [
        'dept',
        'role',
        'status'
    ]


# ---------------- OTP ----------------

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'otp',
        'created_at'
    ]

    search_fields = ['email']


# ---------------- TASK ----------------

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'task_title',
        'task_priority',
        'start_date',
        'end_date',
        'task_type',
        'created_at',
        'updated_at'
    ]

    search_fields = [
        'task_title',
        'task_description'
    ]

    list_filter = [
        'task_priority',
        'task_type'
    ]


# ---------------- TASK ASSIGNMENT ----------------

@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'task',
        'employee',
        'status',
        'assigned_date'
    ]

    search_fields = [
        'task__task_title',
        'employee__first_name',
        'employee__last_name'
    ]

    list_filter = [
        'status',
        'assigned_date'
    ]
    from django.contrib import admin
from .models import PerformanceReview

admin.site.register(PerformanceReview)