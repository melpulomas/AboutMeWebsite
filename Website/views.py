from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("testing 1 2 3!")

# Create your views here.
