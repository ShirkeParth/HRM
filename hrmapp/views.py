from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Department, Role,Employee


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

