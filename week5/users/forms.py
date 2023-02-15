from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Введите имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Введите Фамилию'
    }))

    email = forms.CharField(widget=forms.EmailField(attrs={
        'class': 'input',
        'placeholder': 'Введите почту'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')