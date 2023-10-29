from django.shortcuts import render, redirect
from .models import Store, Product
from .forms import StoreForm, ProductForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores,
    }
    return render(request, 'stores/index.html', context)


def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    products = Product.objects.all()
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            # 입력값 안받아온 애들 
            product.user = request.user
            product.store = store
            product_form.save()
            return redirect('stores:detail', store.pk)
    else:
        product_form = ProductForm()
    context = {
        'store': store,
        'product_form': product_form,
        'products': products
    }
    return render(request, 'stores/detail.html', context)




def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('stores:detail', product.pk)
    else:
        form = StoreForm()
    context ={
        'form': form,
    }
    return render(request, 'stores/create.html', context)