from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

def index(request):
    """Render the index.html page"""
    return render(request, 'index.html')

@login_required
def user_logout(request):
    """Log user out"""
    auth.logout(request)
    messages.success(request, 'You have been logged out...')
    return redirect(reverse('index'))

def user_login(request):
    """Log user in """
    if request.user.is_authenticated:
        return redirect(reverse('index')) 
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid:
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        if user:
            auth.login(request, user)
            messages.success(request, 'You are now logged in. Welcome!')
            return redirect(reverse('index'))
        else:
            messages.success(request, 'There was a problem with your credentials, please try again')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form" : login_form})

def user_registration(request):
    """Render registration page"""
    registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {'registration_form' : registration_form})