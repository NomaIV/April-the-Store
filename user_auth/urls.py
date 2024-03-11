from django.urls import path
from .views import user_login,user_registration, user_logout, password_change, user_profile

app_name ='user_auth'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_registration, name='register'),
    path('password_change/', password_change, name='password_change'),
    path('profile/',user_profile, name='user_profile')
]