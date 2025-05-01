

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
from django.contrib.auth.forms import UserCreationForm

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


def category_list(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    return render(request, 'category_list.html', {'categories': categories, 'items': items})

def weekly_deals(request):
    deals = Item.objects.filter(is_weekly_deal=True)  # You’ll need a field like this
    return render(request, 'weekly_deals.html', {'deals': deals})
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
