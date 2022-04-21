from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

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
