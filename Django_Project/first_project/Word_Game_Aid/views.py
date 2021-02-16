#from django.shortcuts import HttpResponse  #import render


from django.shortcuts import HttpResponse, render

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! Welcome to the World renowned, Word Game Aid 🥳🎃")
    
    
def Scrabble_Aid(request):
    return HttpResponse("Hello, world! Welcome to the Scrabble Aid APP 🧠🕵🏽‍♂️")


def Word_Cookie_Aid(request):
    return HttpResponse("Hello, world! Welcome to the Word Cookie Aid APP 🍪🐿")
    
    
import os

def createSuperUser(request):
    admin = os.system("python manage.py createsuperuser")
    return 
