from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    charasters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charasters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        charasters.extend(list('0123456789'))

    if request.GET.get('special'):
        charasters.extend(list('!#$%&()*+-/][}{><=@&?'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(charasters)
        
    return render(request, 'generator/password.html', {'password':thepassword})