from django.shortcuts import render

# Create your views here.
	
from django.shortcuts import render
from .models import Menu    
from .forms import MenuForm

def index(request):
    form = MenuForm()
    print(form)
    menus = Menu.objects.all()
    context = {
        'menus':menus
    }
    return render(request, 'menus/index.html', context)

def new(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return
    else:
        form = MenuForm()
    
    context = {
        'form': form,
    }
    return render(request, 'menus/new.html', context)

def delete(request, menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    menu.delete()
    return redirect('menus:index')
