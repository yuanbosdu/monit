from django.shortcuts import render

# Create your views here.
from django.http import response
from django.http import request

def index(request):
    return render(request, "index.html")
