from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = { 'no_of_slides': nSlides,'product': products, 'range': range(1, nslides)} 
    return render(request, 'shop/index.html',params )

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('This is contact page')

def tracker(request):
    return HttpResponse('This is tracker page')

def search(request):
    return HttpResponse('This is search page')

def productview(request):
    return HttpResponse('This is productview page')

def checkout(request):
    return HttpResponse('This is checkout page')