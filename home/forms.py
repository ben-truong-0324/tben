# accounts.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
# from django_countries.countries import COUNTRIES

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Your email address', }))
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Subject of message', }))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Your message', }), required=True)

