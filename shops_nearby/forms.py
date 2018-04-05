from django import forms
from django.contrib.gis import geos
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.gis.db import models as gis_models

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    location = forms.CharField(required=True)
    maplocation = gis_models.PointField("longitude/latitude",
                                         geography=True, blank=False, null=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'location', 'maplocation','password1', 'password2', )
