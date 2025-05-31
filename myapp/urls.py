from django.urls import path
from .views import student_list, student_info, student_add, student_delete

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/add/', student_add, name='student_add'),
    path('students/<int:pk>/', student_info, name='student_info'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
]