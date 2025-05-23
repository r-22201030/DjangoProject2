from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Item
from .forms import UserUpdateForm
from .models import Category, Product
from .models import LoyaltyProgram
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Account view
@login_required
def account_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')  # Stay on the same page after update
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'account.html', {'form': form})

# Edit account view
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

# Logout view
def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to home page after logout

# Shop views
def category_list(request):
    categories = Category.objects.all()
    print("CATEGORIES:", categories)  # Debug line
    for c in categories:
        print(f"{c.name} -> Items: {c.items.all()}")  # If using related_name='items'
    return render(request, 'category_list.html', {'categories':categories})
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)  # Fetch category by ID
    items = Item.objects.filter(category=category)  # Get items in the category
    return render(request, 'category_detail.html', {'category': category, 'items': items})

def item_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)  # Fetch category by slug
    items = Item.objects.filter(category=category)  # Get items in the category
    return render(request, 'item_detail.html', {'category': category, 'items': items})
def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
def category_view(request, slug):
    category = Category.objects.get(slug=slug)
    items = category.items.all()  # Access all items related to this category
    return render(request, 'category_detail.html', {'category': category, 'items': items})


def weekly_deals(request):
    return render(request, 'weekly_deals.html')
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = category.items.all()
    return render(request, 'category_detail.html', {'category': category, 'items': items})

def place_order(request, item_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        # Save order logic here...
        # Redirect or show success
        return redirect('order_success')

def order_success(request):
    return render(request, 'order_success.html')


@login_required
def loyalty_rewards(request):
    # Get or create the loyalty program for the user
    loyalty_program, created = LoyaltyProgram.objects.get_or_create(user=request.user)

    # You can update the total spent from a form submission or directly (just a placeholder for now)
    if request.method == 'POST':
        amount_spent = float(request.POST.get('amount_spent', 0))  # Get amount spent from the form
        loyalty_program.update_total_spent(amount_spent)
        loyalty_program.check_reward()

    context = {
        'loyalty_program': loyalty_program
    }
    return render(request, 'loyalty_rewards.html', context)

def loyalty_success(request):
    return render(request, 'update.html')
def popular_items(request):
    popular_products = Item.objects.filter(popular=True)
    return render(request, 'popular_items.html', {'items': popular_products})

def offer_items(request):
    items = Item.objects.filter(Q(has_offer=True) | Q(buy_two_get_one=True))
    return render(request, 'offer_items.html', {'items': items})


def contact_view(request):
    if request.method == 'POST':
        print("Form submitted")
        return redirect('success')
    return render(request, 'contact.html')


def success_view(request):
    return render(request, 'success.html')