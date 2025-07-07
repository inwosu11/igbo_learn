from django import forms
from .models import IgboWord

class IgboWordForm(forms.ModelForm):
    class Meta:
        model = IgboWord
        fields = ['word', 'meaning', 'example_sentence', 'sound_file']