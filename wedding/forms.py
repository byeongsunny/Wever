from django import forms
from .models import wedding

class WeddingForm(forms.ModelForm):
    class Meta:
        model = wedding
        fields = (
            "title",
            "author",
            "phone_number",
            "description",
        )