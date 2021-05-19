from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Projet1(request):
    return render(request,'app1_1/acceuil.html')
