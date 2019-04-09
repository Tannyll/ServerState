from django import forms
from palette.models import Palette


class PaletteForm(forms.ModelForm):
    class Meta:
        model = Palette
        exclude = ('is_deleted',)