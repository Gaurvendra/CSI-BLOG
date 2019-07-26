from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile
class registeru(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name  = forms.CharField()
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email', 'password1', 'password2']
class userupdate(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'email']
class profileupdate(forms.ModelForm):
    class Meta:
        model=profile
        fields = ['image','about']