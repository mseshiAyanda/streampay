from django import forms
from .models import Content

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Content_form(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']        