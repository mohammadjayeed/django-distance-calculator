from .models import DistanceCalculateModel
from django import forms

class DestinationFieldForm(forms.ModelForm):
    class Meta:
        model = DistanceCalculateModel
        fields = ('destination',)