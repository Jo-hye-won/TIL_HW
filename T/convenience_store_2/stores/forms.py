from django import forms
from .models import Store, Product


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'amount', 'price', 'adult',)