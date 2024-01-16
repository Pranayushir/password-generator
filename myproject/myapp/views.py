
import string
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PasswordGeneratorForm
from .models import GeneratedPassword
from django.utils.crypto import get_random_string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    chars = ''
    if include_uppercase:
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if include_lowercase:
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if include_numbers:
        chars += '0123456789'
    if include_symbols:
        chars += '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    return get_random_string(length, chars)

def password_generator(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            include_uppercase = form.cleaned_data['include_uppercase']
            include_lowercase = form.cleaned_data['include_lowercase']
            include_numbers = form.cleaned_data['include_numbers']
            include_symbols = form.cleaned_data['include_symbols']

            password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)

            GeneratedPassword.objects.create(password=password)
            messages.success(request, 'Password generated successfully!')
            return redirect('password_generator')
    else:
        form = PasswordGeneratorForm()

    generated_password = GeneratedPassword.objects.last()

    return render(request, 'password_generator.html', {'form': form, 'generated_passwords': generated_password})


