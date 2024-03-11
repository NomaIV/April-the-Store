from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import AddToCartForm, CheckoutForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Index 
def index(request):
    return render(request, 'index.html', {'current_page': 'index'})

# Product List
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# Home page
def home(request):
    return render(request, 'home.html', {'current_page': 'home'})

# Cart 
@login_required
def cart(request):
    cart_items = request.session.get('cart', [])
    products_in_cart = Product.objects.filter(id__in=cart_items)
    total_price = sum(product.price * product_quantity for product, product_quantity in zip(products_in_cart, cart_items))

    return render(request, 'cart.html', {'products_in_cart': products_in_cart, 'total_price': total_price})

# Contact Information
def contact(request):
    return render(request, 'contact.html')

# Account Information
def account(request):
    return render(request, 'cart.html')

# Product Detail
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartForm(request.POST or None)

    if request.method == 'POST':
        form = AddToCartForm(request.POST or None)
        if form.is_valid():
            # Add product to cart
            messages.success(request, 'Product added to cart successfully.')
            return redirect('cart')
        
        return render(request, 'products.html', {'product': product, 'form': form})

# Checkout
@login_required
def checkout(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = CheckoutForm(request.POST or None)

    if request.method == 'POST':
        form = CheckoutForm(request.POST or None)
        if form.is_valid():
            # Process payment and update order status
            messages.success(request, 'Payment processed successfully.')
            return redirect('home')

        return render(request, 'cart.html', {'product': product, 'form': form})
 
# Products
def products(request):
    return render(request, 'products.html')

# User Profile
@login_required
def user_profile(request):
    user_info = {
        'username': request.user.username,
        'email': request.user.email
    }
    return render(request, 'user_auth/user_profile.html')
    