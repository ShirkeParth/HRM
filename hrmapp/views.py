from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator

import random

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

from .forms import PerformanceReviewForm
# ---------------- DASHBOARD ----------------

def dashboard(request):

    department_count = Department.objects.filter(
        status=True
    ).count()

    role_count = Role.objects.filter(
        status=True
    ).count()

    employee_count = Employee.objects.filter(
        status=True
    ).count()

    task_count = Task.objects.count()

    review_count = PerformanceReview.objects.count()

    leave_count = Leave.objects.count()

    return render(
        request,
        'dashboard.html',
        {
            'department_count': department_count,
            'role_count': role_count,
            'employee_count': employee_count,
            'task_count': task_count,
            'review_count': review_count,
            'leave_count': leave_count,
        }
    )
# ---------------- DEPARTMENT CRUD ----------------
def department_dashboard(request):

    search = request.GET.get('search')

    if search:

        departments = Department.objects.filter(
            dept_name__icontains=search,
            status=True
        )

    else:

        departments = Department.objects.filter(
            status=True
        )

    return render(
        request,
        'department/dashboard.html',
        {
            'departments': departments
        }
    )

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

def add_review(request):

    employee_id = request.session.get('employee_id')

    if not employee_id:
        return redirect('login')

    try:
        current_employee = Employee.objects.get(
            id=employee_id
        )
    except Employee.DoesNotExist:
        return redirect('login')

    if request.method == "POST":

        PerformanceReview.objects.create(
            review_title=request.POST.get('review_title'),
            review_date=request.POST.get('review_date'),
            employee_id=request.POST.get('employee'),
            reviewed_by=current_employee,
            review_period=request.POST.get('review_period'),
            rating=request.POST.get('rating'),
            comments=request.POST.get('comments')
        )

        return redirect('review_dashboard')

    employees = Employee.objects.filter(status=True)

    return render(
        request,
        'review/add_review.html',
        {
            'employees': employees
        }
    )

def review_dashboard(request):

    reviews = PerformanceReview.objects.all()

    search = request.GET.get('search')
    period = request.GET.get('period')

    if search:
        reviews = reviews.filter(
            review_title__icontains=search
        )

    if period:
        reviews = reviews.filter(
            review_period=period
        )

    total_reviews = PerformanceReview.objects.count()

    monthly_reviews = PerformanceReview.objects.filter(
        review_period='Monthly'
    ).count()

    quarterly_reviews = PerformanceReview.objects.filter(
        review_period='Quarterly'
    ).count()

    annual_reviews = PerformanceReview.objects.filter(
        review_period='Annual'
    ).count()

    return render(
        request,
        'review/dashboard.html',
        {
            'reviews': reviews,
            'total_reviews': total_reviews,
            'monthly_reviews': monthly_reviews,
            'quarterly_reviews': quarterly_reviews,
            'annual_reviews': annual_reviews,
        }
    )

def update_review(request, id):

    review = PerformanceReview.objects.get(id=id)

    if request.method == "POST":

        review.review_title = request.POST.get('review_title')
        review.review_date = request.POST.get('review_date')
        review.review_period = request.POST.get('review_period')
        review.rating = request.POST.get('rating')
        review.comments = request.POST.get('comments')

        review.save()

        return redirect('review_dashboard')

    return render(
        request,
        'review/update_review.html',
        {
            'review': review
        }
    )
def delete_review(request, id):

    review = get_object_or_404(
        PerformanceReview,
        id=id
    )

    review.delete()

    return redirect('review_dashboard')

def leave_dashboard(request):

    employee_id = request.session.get('employee_id')

    if not employee_id:
        return redirect('login')

    employee = Employee.objects.get(id=employee_id)

    leaves = Leave.objects.filter(
        employee=employee
    )

    quotas = LeaveQuota.objects.filter(
        employee=employee
    )

    return render(
        request,
        'leave/dashboard.html',
        {
            'leaves': leaves,
            'quotas': quotas
        }
    )

from datetime import datetime
def apply_leave(request):

    employee_id = request.session.get('employee_id')

    if not employee_id:
        return redirect('login')

    employee = Employee.objects.get(
        id=employee_id
    )

    if request.method == "POST":

        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        start = datetime.strptime(
            start_date,
            '%Y-%m-%d'
        )

        end = datetime.strptime(
            end_date,
            '%Y-%m-%d'
        )

        total_days = (
            end - start
        ).days + 1

        Leave.objects.create(
            employee=employee,
            leave_type=request.POST.get('leave_type'),
            reason=request.POST.get('reason'),
            start_date=start_date,
            end_date=end_date,
            total_days=total_days
        )

        return redirect(
            'leave_dashboard'
        )

    return render(
        request,
        'leave/apply_leave.html'
    )

def update_leave(request, id):

    leave = Leave.objects.get(id=id)

    if request.method == "POST":

        leave.leave_type = request.POST.get('leave_type')
        leave.reason = request.POST.get('reason')
        leave.start_date = request.POST.get('start_date')
        leave.end_date = request.POST.get('end_date')

        leave.save()

        return redirect('leave_dashboard')

    return render(
        request,
        'leave/update_leave.html',
        {
            'leave': leave
        }
    )
def approve_leave(request, id):

    return redirect('leave_dashboard')
def leave_quota_dashboard(request):

    return render(
        request,
        'leave/leave_quota.html'
    )


def update_leave(request, id):

    leave = Leave.objects.get(id=id)

    if leave.status != 'Pending':
        return redirect('leave_dashboard')

    if request.method == "POST":

        leave.leave_type = request.POST.get('leave_type')
        leave.reason = request.POST.get('reason')
        leave.start_date = request.POST.get('start_date')
        leave.end_date = request.POST.get('end_date')

        leave.save()

        return redirect('leave_dashboard')

    return render(
        request,
        'leave/update_leave.html',
        {
            'leave': leave
        }
    )

def leave_quota_dashboard(request):

    quotas = LeaveQuota.objects.all()

    paginator = Paginator(
        quotas,
        5
    )

    page_number = request.GET.get('page')

    quotas = paginator.get_page(
        page_number
    )

    return render(
        request,
        'leave/leave_quota.html',
        {
            'quotas': quotas
        }
    )

def update_quota(request, id):

    quota = LeaveQuota.objects.get(id=id)

    if request.method == "POST":

        quota.total_quota = request.POST.get('total_quota')
        quota.used_quota = request.POST.get('used_quota')

        quota.remain_quota = (
            float(quota.total_quota)
            -
            float(quota.used_quota)
        )

        quota.save()

        return redirect(
            'leave_quota_dashboard'
        )

    return render(
        request,
        'leave/update_quota.html',
        {
            'quota': quota
        }
    )

def approve_leave(request, id):

    leave = Leave.objects.get(id=id)

    if request.method == "POST":

        action = request.POST.get('status')

        leave.status = action

        employee_id = request.session.get('employee_id')

        if employee_id:
            leave.approved_by_id = employee_id

        leave.save()

        # Auto Update Leave Quota

        if action == "Approved":

            quota = LeaveQuota.objects.get(
                employee=leave.employee,
                leave_type=leave.leave_type
            )

            quota.used_quota += leave.total_days

            quota.remain_quota = (
                quota.total_quota -
                quota.used_quota
            )

            quota.save()

        return redirect(
            'manager_leave_dashboard'
        )

    return render(
        request,
        'leave/approve_leave.html',
        {
            'leave': leave
        }
    )

def add_leave_quota(request):

    if request.method == "POST":

        employee_id = request.POST.get('employee')

        leave_type = request.POST.get('leave_type')

        total_quota = float(
            request.POST.get('total_quota')
        )

        LeaveQuota.objects.create(
            employee_id=employee_id,
            leave_type=leave_type,
            total_quota=total_quota,
            used_quota=0,
            remain_quota=total_quota
        )

        return redirect(
            'leave_quota_dashboard'
        )

    employees = Employee.objects.all()

    return render(
        request,
        'leave/add_leave_quota.html',
        {
            'employees': employees
        }
    )

def manager_leave_dashboard(request):

    leaves = Leave.objects.all()

    return render(
        request,
        'leave/manager_dashboard.html',
        {
            'leaves': leaves
        }
    )

def leave_dashboard(request):

    employee_id = request.session.get('employee_id')

    if not employee_id:
        return redirect('login')

    employee = Employee.objects.get(
        id=employee_id
    )

    leaves = Leave.objects.filter(
        employee=employee
    )

    search = request.GET.get('search')

    if search:

        leaves = leaves.filter(
            leave_type__icontains=search
        )

    quotas = LeaveQuota.objects.filter(
        employee=employee
    )

    total_leave = leaves.count()

    approved_leave = leaves.filter(
        status='Approved'
    ).count()

    pending_leave = leaves.filter(
        status='Pending'
    ).count()

    rejected_leave = leaves.filter(
        status='Rejected'
    ).count()

    return render(
        request,
        'leave/dashboard.html',
        {
            'leaves': leaves,
            'quotas': quotas,
            'total_leave': total_leave,
            'approved_leave': approved_leave,
            'pending_leave': pending_leave,
            'rejected_leave': rejected_leave,
        }
    )