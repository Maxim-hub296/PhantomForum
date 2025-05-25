from django import forms
from .models import Request, Commentary

class AddRequest(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["target_country", "target_city",
                  "target_name", "target_sin"]

class AddCommentary(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["author", "text"]