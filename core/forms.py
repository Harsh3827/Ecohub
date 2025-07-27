from django import forms
from .models import FAQ

class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your first name'
        })
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your last name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com'
        })
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(555) 123-4567'
        })
    )
    subject = forms.ChoiceField(
        choices=[
            ('', 'Choose a subject'),
            ('general', 'General Inquiry'),
            ('support', 'Technical Support'),
            ('collaboration', 'Collaboration'),
            ('feedback', 'Feedback'),
            ('bug', 'Bug Report'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Tell us how we can help you...'
        })
    )

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'category', 'order']
        widgets = {
            'question': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the question...'
            }),
            'answer': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter the answer...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }, choices=[
                ('General', 'General'),
                ('Articles', 'Articles'),
                ('Tips', 'Tips'),
                ('Account', 'Account'),
                ('Technical', 'Technical'),
            ]),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            })
        } 