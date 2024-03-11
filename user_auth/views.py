from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
    # return render(request, 'cart.html')

# User Registration
def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validate password
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        # Create user
        if len(username) <= 40 and any(char.isalpha() or char in "!@#$%^&*()-_=+" for char in password):
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration successful. Confirmation text sent.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password format.')

    return render(request, 'register.html')

#User Logout
def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect(request, 'logout.html')

# Password Change
def password_change(request):
    if request.method == 'POST':
        username = request.POST['username']
        new_password = request.POST['new_password']

        # Check if the username exists
        if User.objects.filter(username=username).exists():
            # Validate the new password format
            if any(char.isalpha() or char in "!@#$%^&*()-_=+" for char in new_password):
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password changed successfully.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid new password format.')
        else:
            messages.error(request, 'Invalid username.')

    return render(request, 'password_change.html')

# User Profile
def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'user_profile.html', {'user': user})
    else:
        return redirect('login.html')
    
    # return redirect('cart.html')
