from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomAuthenticationForm, CustomUserCreationForm, CustomPasswordChangeForm, \
    CustomPasswordResetForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    success_message = 'You have successfully logged in!'


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy("accounts:password-change-done")
    template_name = 'registration/password_change.html'


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy("accounts:password-reset-done")
    template_name = 'registration/password_reset.html'
