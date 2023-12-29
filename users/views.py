from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=full_name)

                new_profile = CustomUser.objects.create(user=user, phone_number=phone_number)
                new_profile.save()
                
                auth_login(request, user)
                return redirect('signin')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
    
@login_required(login_url='signin')
def signout_view(request):
    auth.logout(request)
    return redirect('signin')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            return redirect('reviews')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def account(request):
    account = CustomUser.objects.get(user=request.user)
    return render(request, 'account.html', {'account' : account})