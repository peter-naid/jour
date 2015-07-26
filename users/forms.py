from django import forms
from .models import ImprovedUser

class LoginForm(forms.ModelForm):
    class Meta:
        model = ImprovedUser
        fields = ["username", "password"]

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = ImprovedUser
        fields = ["username", "password", "email"]
