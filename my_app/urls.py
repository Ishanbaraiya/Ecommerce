"""
URL configuration for my_new_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from .import views
from my_app import views as hv 

urlpatterns = [
    path('admin', admin.site.urls),

    path('',hv.index ,name='index'),
    path('about',hv.about, name='about'),
    path('blog_detail',hv.blog_detail, name='blog_detail'),
    path('blog',hv.blog, name='blog'),
    path('contact',hv.contact, name='contact'),
    path('myaccount',hv.myaccount, name='myaccount'),
    path('update_myaccount/<int:id>',hv.update_myaccount, name='update_myaccount'),
    path('product',hv.product, name='product'),
    path('product_detail/<int:id>',hv.product_detail, name='product_detail'),
    path('shoping_cart',hv.shoping_cart, name='shoping_cart'),
    path('wishlist',hv.wishlist, name='wishlist'),
    path('check_login',hv.check_login, name='check_login'),
    path('creates', hv.creates, name='creates'),
    path('login', hv.login, name='login'),
    path('orders', hv.orders, name='orders'),
    path('signups', hv.signups, name='signups'),
    path('otp', hv.otp, name='otp'),
    path('check_otp', hv.check_otp, name='check_otp'),
    path('reset_pass', hv.reset_pass, name='reset_pass'),
    path('log_out',hv.log_out, name='log_out'),
    path('price_filter',hv.price_filter, name='price_filter'),
    path('color_filter',hv.color_filter, name='color_filter'),
    path('add_cart/<int:id>',hv.add_cart, name='add_cart'),
    path('add_to_wishlist/<int:id>',hv.add_to_wishlist, name='add_to_wishlist'),
    path('search',hv.search, name='search'),
    path('coupon_apply',hv.coupon_apply, name='coupon_apply'),
    path('address',hv.address, name='address'),
    path('add_address',hv.add_address, name='add_address'),
    path('delete_address/<int:id>',hv.delete_address, name='delete_address'),
    path('update_address/<int:id>',hv.update_address, name='update_address'),
    path('add_quantity/<int:id>',hv.add_quantity, name='add_quantity'),
    path('minus_quantity/<int:id>',hv.minus_quantity, name='minus_quantity'),

]
