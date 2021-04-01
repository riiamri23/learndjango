"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from pages.views import homeView, contactView, aboutView, socialView
from products.views import productDetailView, productCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('contact/', contactView),
    path('about/', aboutView),
    path('social/', socialView),
    #product
    path('product/', productDetailView),
    path('product/create', productCreateView)
]
