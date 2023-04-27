from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example1c'}),
                               max_length=200, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example4c'}),
                                required=True, error_messages={'required': 'Please enter a password.'})
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example4cd'}),
                                required=True, error_messages={'required': 'Please enter you  password again.'})

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
