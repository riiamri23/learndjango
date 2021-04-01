# from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductForm

from .models import Product

# Create your views here.
# def homeView(*args, **kwargs):
#     return HttpResponse("<h1>Hello World</h1>") # String of HTML code
def productDetailView(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title':obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object':obj
    }
    return render(request, "products/index.html", context)

def productCreateView(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form': form
    }

    return render(request, "products/create.html", context)
