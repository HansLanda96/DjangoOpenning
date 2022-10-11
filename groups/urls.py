
from django.urls import path

from .views import create_group, delete_group, detail_group, get_groups, update_group

# CRUD      Create, Read, Update, Delete

app_name = 'groups'

urlpatterns = [
    path('create/', create_group, name='create'),                   # Create
    path('', get_groups, name='list'),
    path('detail/<int:group_id>/', detail_group, name='detail'),  # Read
    path('update/<int:group_id>/', update_group, name='update'),  # Update
    path('delete/<int:group_id>/', delete_group, name='delete'),  # Delete
]
