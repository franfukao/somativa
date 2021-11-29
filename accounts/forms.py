from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Consultation
from django import forms
from django.forms import ModelForm, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usern', 'class': 'input-form', }))
        email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'input-form', }))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-form', }))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'input-form', }))


class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ['date']

    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'placeholder': 'Username', 'class': 'input-form', }))


