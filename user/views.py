import re
import django
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .forms import RegisterForm 
# Create your views here.

def register(request):
    if request.method == 'POST': 
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcone {username}, your account is created')
            return redirect('food:index')
    else:
        form = RegisterForm()
        return render(request, 'user/register.html', {'form':form})