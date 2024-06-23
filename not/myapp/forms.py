from django import forms
from .models import Images
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['img']


