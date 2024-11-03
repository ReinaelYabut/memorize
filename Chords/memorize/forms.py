# chords_app/forms.py

from django import forms
from .models import Key, Chord, ChordImage

class KeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ['name']

class ChordForm(forms.ModelForm):
    class Meta:
        model = Chord
        fields = ['key', 'name', 'description']

class ChordImageForm(forms.ModelForm):
    class Meta:
        model = ChordImage
        fields = ['chord', 'image']
