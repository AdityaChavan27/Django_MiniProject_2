from django import forms
from django.core import validators
from django.forms import ModelForm
from.models import login

class loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'
        widgets={
        'Password': forms.PasswordInput(),

        }