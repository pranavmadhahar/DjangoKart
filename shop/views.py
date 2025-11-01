from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Contact
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
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        contact = Contact(
            name = name,
            email = email,
            phone = phone,
            msg = message
        )
        contact.save()

        
       

    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productview(request, product_id):
    # fetch product using the product_id
    product = get_object_or_404(Product, product_id=product_id)
    print(product)
    return render(request, 'shop/productview.html', {'product': product})

def checkout(request):
    return render(request, 'shop/checkout.html')