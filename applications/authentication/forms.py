from django import forms
from django.contrib.auth import forms as auth_forms

from applications.authentication import (
    models as authentication_models,
    strings as authentication_strings
)


class SignUp(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label=authentication_strings.PASSWORD_LABEL,
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        label=authentication_strings.PASSWORD_REPEAT_LABEL,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        strip=False,
    )

    class Meta:
        model = authentication_models.User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'identification_number',
            'picture'
        )
        labels = {
            'username': authentication_strings.USERNAME_LABEL,
            'first_name': authentication_strings.FIRST_NAME_LABEL,
            'last_name': authentication_strings.LAST_NAME_LABEL,
            'identification_number': authentication_strings.IDENTIFICATION_NUMBER_LABEL,
            'picture': authentication_strings.PICTURE_LABEL,
        }
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'identification_number': forms.NumberInput(attrs={"class": "form-control"}),
            'picture': forms.FileInput(attrs={"class": "form-control"}),
        }


class LogIn(auth_forms.AuthenticationForm):
    username = forms.CharField(
        label=authentication_strings.USERNAME_LABEL,
        widget=forms.TextInput(attrs={'autofocus': True, "class": "form-control"})
    )
    password = forms.CharField(
        label=authentication_strings.PASSWORD_LABEL,
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
