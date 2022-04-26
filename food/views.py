
from dataclasses import field
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Item
from .forms import ItemForm 

# Create your views here.

# function base view
def index(request): 
    Item_list = Item.objects.all()
    context = {
        'Item_list'  : Item_list 
    }
    return render(request, 'food/index.html' , context )

# class base view 
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name  = 'Item_list'

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html' , context )

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'
    ## note 
    ## ถ้า ไม่ใส่ 'context_object_name' จะ default เป็น 'object'

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

#  create item class base view 
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_img']
    template_name = 'food/item-form.html'
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)



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

    