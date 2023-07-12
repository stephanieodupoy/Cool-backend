from django import forms
from .models import RecomendedCart


class RecomendedCartForm(forms.ModelForm):
    class Meta:
        model = RecomendedCart
        fields = '__all__'
