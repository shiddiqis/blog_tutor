from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'blog1.html')

# Create your views here.
