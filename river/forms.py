from django import forms
from .models import River


class RiverForm(forms.ModelForm):
    class Meta:
        model = River
        fields = "__all__"

        widgets = {
            "river_name": forms.TextInput(attrs={'class': 'form-control'}),
            "river_length": forms.NumberInput(attrs={'class': 'form-control'}),
            "river_area": forms.NumberInput(attrs={'class': 'form-control'}),
            "flows_in_states": forms.Textarea(attrs={'class': 'form-control'}),
            "river_mode": forms.Select(attrs={'class': 'form-control'}),
        }
