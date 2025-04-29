# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.all_items, name='all_items'),  # Add this URL pattern
]
