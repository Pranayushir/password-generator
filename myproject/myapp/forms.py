
from django import forms

class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(min_value=8, max_value=32, initial=12)
    include_uppercase = forms.BooleanField(required=False, initial=True)
    include_lowercase = forms.BooleanField(required=False, initial=True)
    include_numbers = forms.BooleanField(required=False, initial=True)
    include_symbols = forms.BooleanField(required=False, initial=True)
