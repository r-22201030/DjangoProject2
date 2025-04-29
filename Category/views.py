# views.py
from django.shortcuts import render
from .models import Item
from django.shortcuts import render, get_object_or_404
def all_items(request):
    items = Item.objects.all()  # Fetch all items
    return render(request, 'category.html', {'items': items})


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})
