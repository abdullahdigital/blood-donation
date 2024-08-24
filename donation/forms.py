from django import forms
from .models import Donor, BloodRequest, ContactMessage

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'phone', 'cnic', 'blood_type', 'city', 'address','hospital']

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['blood_type', 'city', 'address', 'phone','hospital']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
