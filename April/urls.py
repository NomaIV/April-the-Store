from April.views import home, contact, cart, product_detail,product_list, account, checkout, index, products
from django.urls import path
from .import views

app_name = 'April'

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product-list/', product_list, name='product_list'),
    path('account/', account, name='account'),
    path('checkout/', checkout, name='checkout'),
    path('products/', products, name='products'),
    path('accounts/profile/', views.user_profile, name='user_profile')
]
