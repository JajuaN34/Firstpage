from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,"firstpage/homepage.html",{})
def andki(request):
    return render(request,"firstpage/giraffe.html",{})