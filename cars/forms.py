from django import forms
from .models import Car

class ImageForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['picture', 'vehicle_model','manufacturer','drive_system','color']
