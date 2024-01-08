from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart
from users.models import CustomUser
from django.contrib.auth.decorators import login_required



def reviews(request):
    products = Product.objects.all()
    return render(request, 'reviews.html', {'products': products})

@login_required(login_url='signin')
def cart(request):
    user = request.user
    custom_user = get_object_or_404(CustomUser, user=user)
    user_cart, created = Cart.objects.get_or_create(user=custom_user)
    
    if isinstance(user_cart, tuple):
        user_cart = user_cart[0] 

    cart_items = user_cart.selected_products.all()
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)

@login_required(login_url='signin')
def remove_from_cart(request, product_id):
    user = request.user
    custom_user = get_object_or_404(CustomUser, user=user)
    user_cart = get_object_or_404(Cart, user=custom_user)
    product = get_object_or_404(Product, id=product_id)
    
    if product in user_cart.selected_products.all():
        user_cart.selected_products.remove(product)
        
    return redirect('cart')  

@login_required(login_url='signin')
def add_to_cart(request, product_id):
    user = request.user
    custom_user = get_object_or_404(CustomUser, user=user)
    user_cart, created = Cart.objects.get_or_create(user=custom_user)
    product = get_object_or_404(Product, id=product_id)

    if not user_cart.selected_products.filter(id=product_id).exists():
        user_cart.selected_products.add(product)
        
    return redirect('cart')
