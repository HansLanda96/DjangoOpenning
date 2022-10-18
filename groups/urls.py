
from django.urls import path

from .views import (ListGroupView, UpdateGroupView, create_group, delete_group,
                    detail_group)

# CRUD      Create, Read, Update, Delete

app_name = 'groups'

urlpatterns = [
    path('create/', create_group, name='create'),                   # Create
    path('', ListGroupView.as_view(), name='list'),
    path('detail/<int:group_id>/', detail_group, name='detail'),  # Read
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),  # Update
    path('delete/<int:group_id>/', delete_group, name='delete'),  # Delete
]
