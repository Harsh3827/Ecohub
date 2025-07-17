from django import forms
from .models import Tip

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['title', 'description', 'category', 'file_upload']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tip title...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 6,
                'placeholder': 'Describe your eco-friendly tip...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'file_upload': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }
