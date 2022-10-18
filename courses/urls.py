from django.urls import path

from .views import (CreateCourseView, DeleteCourseView, DetailCourseView,
                    ListCourseView, UpdateCourseView)

app_name = 'courses'

urlpatterns = [
    path('', ListCourseView.as_view(), name='list'),
    path('create/', CreateCourseView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailCourseView.as_view(), name='detail'),
    path('edit/<int:pk>/', UpdateCourseView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteCourseView.as_view(), name='delete'),
]
