from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create_department/', views.create_department, name='create_department'),
    path('update_department/<int:id>/', views.update_department, name='update_department'),
    path('delete_department/<int:id>/', views.delete_department, name='delete_department'),
]