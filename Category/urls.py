# urls.py
from django.urls import path
from . import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.category_list, name='category_list'),  # Add this URL pattern
]
