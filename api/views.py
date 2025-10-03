from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def TestView(request):
    return HttpResponse("Welcome to out Test View")
    
def TeachView(request):
    return HttpResponse("This is Teacher view")

