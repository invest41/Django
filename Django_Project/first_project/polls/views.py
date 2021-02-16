#from django.shortcuts import HttpResponse  #import render



from django.http import HttpResponse
from django.shortcuts import render
from .models import Poll, Offer


# Create your views here.

def index(request):
    polls = Poll.objects.all()
    return render(request, 'index1.html', {'polls': polls})
    
    
    #return HttpResponse("Hello, world. You're at the products index.")
    
    
import os

def createSuperUser(request):
    admin = os.system("python manage.py createsuperuser")
    return 
