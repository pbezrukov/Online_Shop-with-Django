"""SHOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from products.views import home, all, single, search
from carts.views import view, add_to_cart, remove_from_cart
from django.conf.urls.static import static
from orders.views import checkout, orders

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^s/$', search, name='search'),
    url(r'^products/$', all, name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$', single, name='single_product'),
    url(r'^cart/(?P<id>\d+)/$', remove_from_cart, name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', add_to_cart, name='add_to_cart'),
    url(r'^cart/$', view, name='view'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^orders/$', orders, name='user_orders'),
    path('admin/', admin.site.urls),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


