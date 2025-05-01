

from django.shortcuts import render
from .models import Product
from django.shortcuts import render
from .models import Category
from .models import Item

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
# views.py
from django.shortcuts import render, get_object_or_404


from django.shortcuts import render, get_object_or_404
from .models import Category


# views.py

from django.shortcuts import render, redirect
# views.py
from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Home page e redirect hobe
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def home_view(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace with your homepage view name
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def account_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')  # Redirect to same page after update
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'account.html', {'form': form})

@login_required
def edit_account_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')  # Redirect to account view after update
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'account.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')