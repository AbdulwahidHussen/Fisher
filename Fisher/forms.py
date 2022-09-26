from django import forms
from django.contrib.auth.models import User
from.models import Info
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserInfo(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'
class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password")

        widgets = {
            'password': forms.PasswordInput(attrs={'type':'password','palceholder':'password'}),

        }

