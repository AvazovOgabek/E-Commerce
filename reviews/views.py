from django.shortcuts import render
from .models import Product

def reviews(request):
    products = Product.objects.all()
    return render(request, 'reviews.html', {'products' : products})
