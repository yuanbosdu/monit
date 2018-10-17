from django.shortcuts import render

# Create your views here.

from homepage.tasks import mul

def index(request):
    #mul.delay(100, 100)
    return render(request, "index.html")
