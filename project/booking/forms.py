
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    
    scheduled_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",  
                "class": "form-control"
            }
        ),
        input_formats=["%Y-%m-%dT%H:%M"],  
    )

    class Meta:
        model = Booking
        fields = ["scheduled_date", "description"]
        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 3, 
                "class": "form-control"
            }),
        }
