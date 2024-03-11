from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Registration Form
class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=40, help_text='Maximum 40 characters')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Include letters and special characters')
    confirm_password = forms.CharField(widget=forms.PasswordInput, help_text='Include letters and special characters')
# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, help_text='Maximum 40 characters')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Include letters and special characters')

# Password Change Form
class PasswordChangeForm(forms.Form):
    username = forms.CharField(max_length=40, help_text='Maximum 40 characters')
    new_password = forms.CharField(widget=forms.PasswordInput, help_text='Include letters and special characters')

