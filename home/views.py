from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

def index(request):

    return render(request, 'home/home.html')

def contact(request):
    
    return render(request, 'home/contact.html')