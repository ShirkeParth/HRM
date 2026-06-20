from django.contrib import admin

from .models import (
    Department,
    Role,
    Employee,
    OTP,
    Task,
    TaskAssignment,
    PerformanceReview,
    Leave,
    LeaveQuota
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


# ---------------- PERFORMANCE REVIEW ----------------

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'review_title',
        'employee',
        'reviewed_by',
        'review_period',
        'rating',
        'review_date'
    ]

    search_fields = [
        'review_title',
        'employee__first_name',
        'employee__last_name'
    ]

    list_filter = [
        'review_period',
        'review_date'
    ]


# ---------------- LEAVE ----------------

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'employee',
        'leave_type',
        'start_date',
        'end_date',
        'total_days',
        'status',
        'approved_by'
    ]

    search_fields = [
        'employee__first_name',
        'employee__last_name'
    ]

    list_filter = [
        'leave_type',
        'status'
    ]


# ---------------- LEAVE QUOTA ----------------

@admin.register(LeaveQuota)
class LeaveQuotaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'employee',
        'leave_type',
        'total_quota',
        'used_quota',
        'remain_quota'
    ]

    search_fields = [
        'employee__first_name',
        'employee__last_name'
    ]

    list_filter = [
        'leave_type'
    ]