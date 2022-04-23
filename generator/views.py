from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    
    charasters = list('abcdefghijklmnopqrstuvwxyz')
    length = 10
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(charasters)
        
    return render(request, 'generator/password.html', {'password':thepassword})