from django import forms

class DestinationFieldForm(forms.Form):
    
    destination = forms.CharField(max_length=200)