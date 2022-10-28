from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import ProcessFormView

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


class AccountRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/register.html'


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Welcome, {self.request.user.username}!')
        return response


class AccountLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'


class AccountUpdateView(LoginRequiredMixin, ProcessFormView):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)
        return render(request, 'accounts/update.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserUpdateForm(data=request.POST, instance=user)
        profile_form = ProfileUpdateForm(data=request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('accounts:profile_view'))


@login_required
def account_view(request):
    return render(request, 'accounts/profile_view.html')
