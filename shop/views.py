from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    all_products = {}

    for cat in categories:
        products = list(Product.objects.filter(category=cat))
        # Group into chunks of 4
        slides = [products[i:i+4] for i in range(0, len(products), 4)]
        
        all_products[cat] = {
            "slides": slides,
            "slide_count": len(slides)
        }

    return render(request, 'shop/index.html', {'all_products': all_products})


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