from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'id': 'name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'id': 'email'
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'id': 'subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'id': 'message'
    }))
