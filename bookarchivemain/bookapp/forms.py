from django import forms
from .models import *


class PartsForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = '__all__'
