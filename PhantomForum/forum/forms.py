from django import forms
from .models import Request

class AddRequest(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["target_country", "target_city",
                  "target_name", "target_sin"]
