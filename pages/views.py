from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request,"home.html",{})
def product2_view(request,*args, **kwargs):
    details = {
        "product" : "Apple phone"
    }
    return render(request,"product2.html",details)
def product1_view(*args, **kwargs):
    return HttpResponse("<h1>Apple Watch</h1>")
    