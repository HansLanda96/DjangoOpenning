"""teachers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path    # noqa

from teachers.views import create_teacher, delete_teacher, detail_teacher, get_teachers, update_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('detail/<int:teacher_id>/', detail_teacher, name='detail'),
    path('edit/<int:teacher_id>/', update_teacher, name='update'),
    path('delete/<int:teacher_id>/', delete_teacher, name='delete'),
]
