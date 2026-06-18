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
]