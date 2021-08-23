from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User

from registration.forms import NewUserForm

# Create your views here.
def index(request):
    """Index page for initial web access."""
    return render(request, "registration/index.html")

def signup(request):
    """User sign up or register view."""
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"You've signed up in as {username}")
            return redirect('registration:home', args=(username,))
        else:
            messages.error(request, "Invalid user data")
    else:
        form = NewUserForm()    
    return render(request, "registration/signup.html", {
        "form": form,
    })

def login_user(request):
    """User signin or login view."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You're now logged in as {username}")
                return redirect('registration:home', args=(username,))
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid user or password")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {
        "form": form
    })

def logout_user(request):
    """Logout user."""
    logout(request)
    messages.info(request, "You have successfully logged out!")
    return redirect("registration:index")

def reset_password(request):
    """Reset user password."""
    pass

def home(request, username):
    """Homepage."""
    user = User.objects.get(username=username)

    return render(request, "registration/home.html",{
        "user": user,
    })