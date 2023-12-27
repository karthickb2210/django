from django.shortcuts import render
from .models import Products
# Create your views here.
from .forms import ProductForm,RawProductForm

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
      
    context = {
        'form' : form
    }
    
    return render(request,"search.html",context)

def create_product(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Products.objects.create(**my_form.cleaned_data)
        else:
          print(my_form.errors)
    context = {
        "form" : my_form
    }
    return render(request,"puredjangoform.html",context)


def product_view(request):
    obj = Products.objects.get(id=1)
    context = {
        'title' : obj.title
    }
    
    return render(request,"details.html",context)
