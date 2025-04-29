

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
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid credentials"
    return render(request, 'login.html', {'error': error})
