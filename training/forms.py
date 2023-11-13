from django.forms import ModelForm
from .models import Student
from django import forms

class studentform(ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailInput()
    phone = forms.TextInput()
    choice = (
        ('Ethiopia', 'Ethiopia'),
        ('South Africa', 'South Africa'),
        ('Canada', 'Canada'),
        ('Eritrea', 'Eritrea'),
        ('Other', 'Other'),
    )
    country = forms.ChoiceField(choices=choice, widget=forms.Select())
    expectation = forms.Textarea()

    class Meta:
        model = Student
        fields = [
            'first_name', 
            'last_name',
            'email',
            'phone',
            'country',
            'expectation',
            ]