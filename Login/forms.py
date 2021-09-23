from django import forms
from django.core.exceptions import ValidationError
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=30, label="username",
                               error_messages={"required": "Username cannot be empty",
                                               "min_length": "Username needs to be at least 3 characters."})
    password = forms.CharField(min_length=8, max_length=25, widget=forms.PasswordInput, label="password",
                               error_messages={"required": "Password cannot be empty",
                                                "min_length": "Password should be at least 8 characters."})

class SignupForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=30, label="username",
                               error_messages={"required": "Username cannot be empty",
                                                "min_length": "Username needs to be at least 3 characters."})
    password = forms.CharField(min_length=8, max_length=25, widget=forms.PasswordInput, label="password",
                               error_messages={"required": "Password cannot be empty",
                                               "min_length": "Password should be at least 8 characters."})
    re_input = forms.CharField(max_length=25, widget=forms.PasswordInput, label="validation")
    email = forms.CharField(min_length=6, label="email",
                            error_messages={"required": "Email cannot be empty",
                                            "min_length": "Email should be at least 6 characters."})

    def check(self):
        pass1 = self.cleaned_data.get("password")
        pass2 = self.cleaned_data.get("re_input")

        if pass1 != pass2:
            raise ValidationError("The validation does not match.")
        else:
            return self.cleaned_data
