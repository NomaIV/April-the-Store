from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import AddToCartForm, CheckoutForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Index 
def index(request):
    """
    Render index page.

    :param request: HTTP request object.
    :return: Rendered index page.
    :rtype: django.http.HttpResponse.
    """
    return render(request, 'index.html', {'current_page': 'index'})

# Product List
def product_list(request):
    """
    Render product list page.

    :param request: HTTP request object.
    :return: Rendered product list page.
    :rtype: django.http.HttpResponse.
    """
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# Home page
def home(request):
    """
    Render home page.

    :param request: HTTP request object.
    :return: Rendered home page.
    :rtype: django.http.HttpResponse.
    """
    return render(request, 'home.html', {'current_page': 'home'})

# Cart 
@login_required
def cart(request):
    """
    Render cart page.

    :param request: HTTP request object.
    :return: Rendered cart page.
    :rtype: django.http.HttpResponse.
    """
    cart_items = request.session.get('cart', [])
    products_in_cart = Product.objects.filter(id__in=cart_items)
    total_price = sum(product.price * product_quantity for product, product_quantity in zip(products_in_cart, cart_items))

    return render(request, 'cart.html', {'products_in_cart': products_in_cart, 'total_price': total_price})

# Contact Information
def contact(request):
    """
    Render contact page.

    :param request: HTTP request object.
    :return: Rendered contact page.
    :rtype: django.http.HttpResponse.
    """
    return render(request, 'contact.html')

# Account Information
def account(request):
    """
    Render account page.

    :param request: HTTP request object.
    :return: Rendered account page.
    :rtype: django.http.HttpResponse.
    """
    return render(request, 'cart.html')

# Product Detail
def product_detail(request, product_id):
    """
    Render product detail page and product addition to cart.

    :param request: HTTP request object.
    :param product_id: ID of the product.
    :return: Rendered product detail page.
    :rtype: django.http.HttpResponse.
    """
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
    """
    Render checkout page and process payment.

    :param request: HTTP request object.
    :param product_id: The ID of the product.
    :return: Rendered checkout page.
    :rtype: django.http.HttpResponse.
    """
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
    """
    Render products page.

    :param request: HTTP request object.
    :return: Rendered products page.
    :rtype: django.http.HttpResponse.
    """
    return render(request, 'products.html')

# User Profile
@login_required
def user_profile(request):
    """
    Render the user profile page.

    :param request: The HTTP request object.
    :return: Rendered user profile page.
    :rtype: django.http.HttpResponse.
    """
    user_info = {
        'username': request.user.username,
        'email': request.user.email
    }
    return render(request, 'user_auth/user_profile.html')
    