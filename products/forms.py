from django import forms
    
from .models import Products

class ProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = [
            'id',
            'title',
            'price', 
            'description'
        ]


class RawProductForm(forms.Form):
    id = forms.CharField()
    title = forms.CharField()
    description = forms.CharField()
    price = forms.CharField()

