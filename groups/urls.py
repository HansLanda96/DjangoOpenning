
from django.urls import path

from .views import (CreateGroupView, DeleteGroupView, DetailGroupView,
                    ListGroupView, UpdateGroupView)

# CRUD      Create, Read, Update, Delete

app_name = 'groups'

urlpatterns = [
    path('create/', CreateGroupView.as_view(), name='create'),                   # Create
    path('', ListGroupView.as_view(), name='list'),
    path('detail/<int:pk>/', DetailGroupView.as_view(), name='detail'),  # Read
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),  # Update
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete'),  # Delete
]
