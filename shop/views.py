from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
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
        
        thank = False

        if request.method == 'POST':
            items_json = request.POST.get('itemsJson', '')
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            address = request.POST.get('address1', '') + request.POST.get('address2', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')

            order = Order(
                items_json = items_json,
                name = name,
                email = email,
                phone = phone,
                address = address,
                city = city,
                state = state,
                zip_code = zip_code
            )

            order.save()
            orderId = order.order_id
            update = OrderUpdate(
                order_id = orderId, 
                update_desc = "Your order has been placed"
            )
            update.save()
            thank = True

            return render(request, 'shop/checkout.html', {'thank':thank, 'orderId': orderId})
        
        return render(request, 'shop/checkout.html')
            


        