from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page

    # Authentication paths
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('account/', views.account_view, name='account'),
    path('account/edit/', views.edit_account_view, name='edit_account'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='passchange.html',
        success_url='/account/'
    ), name='password_change'),
    path('logout/', views.logout_view, name='logout'),

    # Category paths
    path('category/<slug:slug>/', views.category_view, name='category'),

    path('categories/', views.category_list, name='category_list'),  # All categories
    path('category/<int:id>/', views.category_detail, name='category_detail'),
    path('item/<int:id>/', views.item_list, name='item_list'),# Category detail with items
    path('weekly-deals/', views.weekly_deals, name='weekly_deals'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('order/<int:item_id>/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),

    path('loyalty-rewards/', views.loyalty_rewards, name='loyalty_rewards'),

    path('loyalty-success/', views.loyalty_success, name='loyalty_success'),
    path('popular/', views.popular_items, name='popular_items'),


]
