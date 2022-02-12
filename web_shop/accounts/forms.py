from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from django.forms import Form, ModelForm


class ProfileEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
