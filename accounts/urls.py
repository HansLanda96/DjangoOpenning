from django.urls import path

from .views import AccountLoginView, AccountLogoutView, AccountRegisterView, AccountUpdateView, account_view

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', account_view, name='profile_view'),
    path('update/', AccountUpdateView.as_view(), name='profile_update'),
]
