from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from .models import Item
from .forms import ItemForm 

# Create your views here.
def index(request): 
    Item_list = Item.objects.all()
    context = {
        'Item_list'  : Item_list 
    }
    return render(request, 'food/index.html' , context )

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html' , context )

def item(request):
    return HttpResponse('<h1> item views </h1>')

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {
        'form':form
    }
    return render(request, 'food/item-form.html', context  )

def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {
        'form':form
    }
    return render(request, 'food/item-form.html', context  )

def delete_item(request, id):
    item = Item.objects.get(pk=id)
    if request.method == 'POST': 
        item.delete()
        return redirect('food:index')
    context = {
        'item':item
    }
    return render(request, 'food/item-delete.html', context )

    