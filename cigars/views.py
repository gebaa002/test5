from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Projet3(request):
    return render(request,'cigars/acceuil.html')
