from django.shortcuts import render, redirect
from .models import Store, Product
from .forms import StoreForm, ProductForm
from django.contrib.auth.decorators import login_required

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


def update(request, pk):
    stores = Store.objects.get(pk=pk)
    if request.user == stores.user:
        if request.method == 'POST':
            form = StoreForm(request.POST, instance=stores)
            if form.is_valid():
                form.save()
                return redirect('stores:detail', stores.pk)
        else:
            form =StoreForm(instance=stores)
    else:
        return redirect('stores:index')
    context ={
        'stores': stores,
        'form': form,
    }
    return render(request, 'stores/update.html', context)

@login_required
def delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('stores:index')