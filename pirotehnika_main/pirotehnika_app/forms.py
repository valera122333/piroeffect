from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'input_class_form'}))
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={'class': 'input_class_form'}))
    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input_class_form'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'input_class_form'}))


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'input_class_form'}))
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input_class_form'}))
