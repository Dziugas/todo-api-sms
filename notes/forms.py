from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')

class DeleteNote(forms.ModelForm):
    class Meta:
        model = Notes
        fields = []