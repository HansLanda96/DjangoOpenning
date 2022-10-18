from django.urls import path

from .views import (UpdateStudentView, create_student, delete_student,
                    detail_student, get_students)

app_name = 'students'

urlpatterns = [
    path('create/', create_student, name='create'),                   # Create
    path('', get_students, name='list'),
    path('detail/<int:student_id>/', detail_student, name='detail'),  # Read
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),  # Update
    path('delete/<int:student_id>/', delete_student, name='delete'),  # Delete
]
