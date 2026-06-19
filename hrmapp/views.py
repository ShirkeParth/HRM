from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import OTP
import random
from .models import Task
from .models import Department, Role, Employee, Task, TaskAssignment
# ---------------- DASHBOARD ----------------

def dashboard(request):
    search = request.GET.get('search')

    if search:
        departments = Department.objects.filter(
            dept_name__icontains=search,
            status=True
        )
    else:
        departments = Department.objects.filter(status=True)

    return render(request, 'department/dashboard.html', {
        'departments': departments
    })


# ---------------- DEPARTMENT CRUD ----------------


def create_department(request):
    if request.method == "POST":
        dept_name = request.POST.get('dept_name')
        description = request.POST.get('description')

        Department.objects.create(
            dept_name=dept_name,
            description=description
        )
        return redirect('dashboard')

    return render(request, 'department/create_department.html')



def update_department(request, id):
    department = Department.objects.get(dept_id=id)

    if request.method == "POST":
        department.dept_name = request.POST.get('dept_name')
        department.description = request.POST.get('description')
        department.save()
        return redirect('dashboard')

    return render(request, 'department/update_department.html', {
        'department': department
    })


def delete_department(request, id):
    department = Department.objects.get(dept_id=id)
    department.status = False
    department.save()
    return redirect('dashboard')


# ---------------- ROLE DASHBOARD ----------------

def role_dashboard(request):
    search = request.GET.get('search')

    if search:
        roles = Role.objects.filter(
            role_name__icontains=search,
            status=True
        )
    else:
        roles = Role.objects.filter(status=True)

    return render(request, 'Role/dashboard.html', {   # ✅ IMPORTANT FIX
        'roles': roles
    })


# ---------------- ROLE CRUD ----------------

def create_role(request):
    if request.method == "POST":
        role_name = request.POST.get('role_name')
        description = request.POST.get('description')

        Role.objects.create(
            role_name=role_name,
            description=description
        )
        return redirect('role_dashboard')

    return render(request, 'Role/create_role.html')



def update_role(request, id):
    role = Role.objects.get(id=id)

    if request.method == "POST":
        role.role_name = request.POST.get('role_name')
        role.description = request.POST.get('description')
        role.save()
        return redirect('role_dashboard')

    return render(request, 'Role/update_role.html', {
        'role': role
    })



def delete_role(request, id):
    role = Role.objects.get(id=id)
    role.status = False
    role.save()
    return redirect('role_dashboard')

def employee_dashboard(request):

    search = request.GET.get('search')

    if search:
        employees = Employee.objects.filter(
            first_name__icontains=search,
            status=True
        )
    else:
        employees = Employee.objects.filter(
            status=True
        )

    return render(
        request,
        'employee/dashboard.html',
        {
            'employees': employees
        }
    )

def create_employee(request):

    if request.method == "POST":

        Employee.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            dept_id=request.POST.get('dept'),
            role_id=request.POST.get('role'),
            reporting_manager_id=request.POST.get('reporting_manager'),
            date_of_joining=request.POST.get('date_of_joining')
        )

        return redirect('employee_dashboard')

    departments = Department.objects.filter(status=True)
    roles = Role.objects.filter(status=True)
    managers = Employee.objects.filter(status=True)

    return render(
        request,
        'employee/create_employee.html',
        {
            'departments': departments,
            'roles': roles,
            'managers': managers
        }
    )

def update_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":

        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.email = request.POST.get('email')
        employee.mobile = request.POST.get('mobile')
        employee.username = request.POST.get('username')
        employee.password = request.POST.get('password')

        employee.dept_id = request.POST.get('dept')
        employee.role_id = request.POST.get('role')
        employee.reporting_manager_id = request.POST.get('reporting_manager')

        employee.date_of_joining = request.POST.get('date_of_joining')

        employee.save()

        return redirect('employee_dashboard')

    departments = Department.objects.filter(status=True)
    roles = Role.objects.filter(status=True)
    managers = Employee.objects.filter(status=True)

    return render(
        request,
        'employee/update_employee.html',
        {
            'employee': employee,
            'departments': departments,
            'roles': roles,
            'managers': managers
        }
    )

def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.status = False
    employee.save()

    return redirect('employee_dashboard')

def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            employee = Employee.objects.get(
                username=username,
                password=password,
                status=True
            )

            request.session['employee_id'] = employee.id

            return redirect('dashboard')

        except Employee.DoesNotExist:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(
        request,
        'auth/login.html'
    )

def forgot_password(request):

    if request.method == "POST":

        email = request.POST.get('email')

        try:

            employee = Employee.objects.get(
                email=email
            )

            otp = str(random.randint(100000,999999))

            OTP.objects.create(
                email=email,
                otp=otp
            )

            send_mail(
                'HRM Password Reset OTP',
                f'Your OTP is {otp}',
                'yourgmail@gmail.com',
                [email],
                fail_silently=False
            )

            request.session['reset_email'] = email

            return redirect('verify_otp')

        except Employee.DoesNotExist:

            messages.error(
                request,
                "Email not found"
            )

    return render(
        request,
        'auth/forgot_password.html'
    )

def verify_otp(request):

    if request.method == "POST":

        otp = request.POST.get('otp')

        email = request.session.get(
            'reset_email'
        )

        try:

            OTP.objects.filter(
                email=email,
                otp=otp
            ).latest('created_at')

            return redirect(
                'reset_password'
            )

        except:

            messages.error(
                request,
                "Invalid OTP"
            )

    return render(
        request,
        'auth/verify_otp.html'
    )

def reset_password(request):

    if request.method == "POST":

        new_password = request.POST.get(
            'password'
        )

        email = request.session.get(
            'reset_email'
        )

        employee = Employee.objects.get(
            email=email
        )

        employee.password = new_password
        employee.save()

        messages.success(
            request,
            "Password Updated Successfully"
        )

        return redirect(
            'login'
        )

    return render(
        request,
        'auth/reset_password.html'
    )

from django.contrib import messages

def logout_view(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('login')

def create_task(request):

    if request.method == "POST":

        Task.objects.create(
            task_title=request.POST.get('task_title'),
            task_description=request.POST.get('task_description'),
            task_priority=request.POST.get('task_priority'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            task_type=request.POST.get('task_type')
        )

        return redirect('task_dashboard')

    return render(
        request,
        'task/create_task.html'
    )

def task_dashboard(request):

    tasks = Task.objects.all()

    return render(
        request,
        'task/dashboard.html',
        {
            'tasks': tasks
        }
    )

def assign_task(request):

    if request.method == "POST":

        TaskAssignment.objects.create(

            task_id=request.POST.get('task'),

            employee_id=request.POST.get('employee')

        )

        return redirect('task_dashboard')

    tasks = Task.objects.all()

    employees = Employee.objects.filter(
        status=True
    )

    return render(
        request,
        'task/assign_task.html',
        {
            'tasks': tasks,
            'employees': employees
        }
    )

def update_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == "POST":

        task.task_title = request.POST.get('task_title')
        task.task_description = request.POST.get('task_description')
        task.task_priority = request.POST.get('task_priority')
        task.start_date = request.POST.get('start_date')
        task.end_date = request.POST.get('end_date')
        task.task_type = request.POST.get('task_type')

        task.save()

        return redirect('task_dashboard')

    return render(
        request,
        'task/update_task.html',
        {
            'task': task
        }
    )

def delete_task(request, id):

    task = Task.objects.get(id=id)

    task.delete()

    return redirect(
        'task_dashboard'
    )

def assignment_dashboard(request):

    assignments = TaskAssignment.objects.all()

    return render(
        request,
        'task/assignment_dashboard.html',
        {
            'assignments': assignments
        }
    )

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

class OTPAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'otp',
        'created_at'
    ]

    search_fields = ['email']


# ---------------- TASK ----------------

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

def update_assignment(request, id):

    assignment = TaskAssignment.objects.get(id=id)

    if request.method == "POST":

        assignment.status = request.POST.get('status')
        assignment.save()

        return redirect('assignment_dashboard')

    return render(
        request,
        'task/update_assignment.html',
        {
            'assignment': assignment
        }
    )