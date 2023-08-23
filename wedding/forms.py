from django import forms
from .models import wedding

class WeddingForm(forms.ModelForm):
    class Meta:
        model = wedding
        fields = (
            "author",
            "phone_number",
            "description",
        )