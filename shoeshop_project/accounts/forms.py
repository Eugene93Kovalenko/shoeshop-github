from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your username'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Your password'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Your password'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Your email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Your password'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

