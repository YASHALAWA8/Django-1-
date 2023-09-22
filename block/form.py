from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        help_text='Номер телефона. Формат +7910...', label='Телефон'
    )
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Одна большая буква и т.д.',
    )

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'password1', 'password2', )