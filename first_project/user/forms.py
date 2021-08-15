from django import forms
from django.forms import widgets
from user.models import User

class SigninForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
        widgets = {
            'password':forms.PasswordInput(),
        }