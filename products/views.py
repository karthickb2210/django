from django.shortcuts import render
from .models import Products
# Create your views here.

def product_view(request):
    obj = Products.objects.get(id=1)
    context = {
        'title' : obj.title
    }
    
    return render(request,"details.html",context)
