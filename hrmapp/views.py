from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    ...

@login_required
def create_department(request):
    ...

@login_required
def update_department(request, id):
    ...

@login_required
def delete_department(request, id):
    ...
# Create your views here.
from django.shortcuts import render, redirect
from .models import Department


def dashboard(request):
    search = request.GET.get('search')
    if search:
        departments = Department.objects.filter(
            dept_name__icontains=search,
            status=True
        )
    else:
        departments = Department.objects.filter(status=True)
    context = {
        'departments': departments
    }
    return render(request, 'department/dashboard.html', context)


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

    context = {
        'department': department
    }

    return render(
        request,
        'department/update_department.html',
        context
    )


def delete_department(request, id):
    department = Department.objects.get(dept_id=id)
    department.status = False
    department.save()
    return redirect('dashboard')