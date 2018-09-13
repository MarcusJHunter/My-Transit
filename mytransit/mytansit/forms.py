from django import forms
from django.contrib.auth.models import User

from .models import Event
from .models import Profile




class LoginForm(forms.Form):
  # class Meta:
  #   model: User
  #   fields=['username', 'password']
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ('first_name','picture', 'email', 'interest',)
