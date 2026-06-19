from django.urls import path
from . import views

urlpatterns = [
    # Department URLs
    path('', views.dashboard, name='dashboard'),
    path('create_department/', views.create_department, name='create_department'),
    path('update_department/<int:id>/', views.update_department, name='update_department'),
    path('delete_department/<int:id>/', views.delete_department, name='delete_department'),

    # Role URLs
    path('roles/', views.role_dashboard, name='role_dashboard'),
    path('create_role/', views.create_role, name='create_role'),
    path('update_role/<int:id>/', views.update_role, name='update_role'),
    path('delete_role/<int:id>/', views.delete_role, name='delete_role'),
    path('employees/',views.employee_dashboard, name='employee_dashboard'),
    path('create_employee/',views.create_employee, name='create_employee'),
    path('update_employee/<int:id>/',views.update_employee,name='update_employee'),
    path('delete_employee/<int:id>/', views.delete_employee,  name='delete_employee'),
    path( 'login/', views.login_view,name='login'),
    path( 'forgot-password/', views.forgot_password,  name='forgot_password'),
    path('verify-otp/', views.verify_otp,name='verify_otp'),
    path('reset-password/',views.reset_password,name='reset_password'),
    path('logout/', views.logout_view, name='logout'),
    path('task/create/',views.create_task,name='create_task'),
    path('tasks/', views.task_dashboard, name='task_dashboard'),
    path('task/assign/', views.assign_task,name='assign_task'),
    path('task/update/<int:id>/',views.update_task,name='update_task'),
    path('task/delete/<int:id>/',views.delete_task, name='delete_task'),
    path('assignments/', views.assignment_dashboard,name='assignment_dashboard'),
    path('assignment/update/<int:id>/', views.update_assignment, name='update_assignment'),
]