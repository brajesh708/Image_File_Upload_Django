from django import forms
from .models import ItemInfo

class ItemInfoForm(forms.ModelForm):
    class Meta:
        model = ItemInfo
        fields = "__all__"