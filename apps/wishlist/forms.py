from django import forms
from .models import Wish


class WishListForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = '__all__'
