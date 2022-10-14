from django.urls import path

from .views import create_course, delete_course, detail_course, get_course, update_course

# CRUD      Create, Read, Update, Delete

app_name = 'courses'

urlpatterns = [
    path('create/', create_course, name='create'),                   # Create
    path('', get_course, name='list'),
    path('detail/<int:course_id>/', detail_course, name='detail'),  # Read
    path('update/<int:course_id>/', update_course, name='update'),  # Update
    path('delete/<int:course_id>/', delete_course, name='delete'),  # Delete
]
