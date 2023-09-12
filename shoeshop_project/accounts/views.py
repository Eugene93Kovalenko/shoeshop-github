from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomAuthenticationForm, CustomUserCreationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("products:home")
    template_name = 'registration/registration.html'
