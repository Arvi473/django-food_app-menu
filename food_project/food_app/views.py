from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    #template = loader.get_template('food_app/index.html')
    context = {
        'item_list':item_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'food_app/index.html',context)

class IndexClassView(ListView):
    model = Item;
    template_name = 'food_app/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse('This is an item view')

#def recipe(request):
    #return HttpResponse('Need the recipe of biryani')

#def rating(request):
    #return HttpResponse('Biryani = 5 star rating')

#def review(request):
    #return HttpResponse('<h1>The taste of this biryani is so delicious here!</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }

    return render(request,'food_app/detail.html',context)

class Food_appDetail(DetailView):
    model = Item;
    template_name = 'food_app/detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food_app:index')
    
    return render(request,'food_app/item-form.html',{'form':form})

#this is a class based view for create item

class CreateItem(CreateView):
    model = Item;
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food_app/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food_app:index')
    
    return render(request,'food_app/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food_app:index')
    
    return render(request,'food_app/item-delete.html',{'item':item})

#def detail(request,item_id):
    #return HttpResponse("This is item no/id: %s" % item_id)