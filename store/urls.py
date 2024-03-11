"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from April.views import index, home, contact, cart, product_detail, product_list, account,checkout, products, user_profile
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


# April and user_auth apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('products/', product_list, name='product_list'),
    path('account/', account, name='account'),
    path('checkout/', checkout, name='checkout'),
    path('products/', products, name='products'),
    path('accounts/', include('user_auth.urls', namespace='user_auth')),  # User_auth URLs
    path('accounts/profile/', user_profile, name='user_profile'),


# Authentication urls
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
