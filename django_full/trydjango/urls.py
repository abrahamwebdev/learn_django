"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from pages import views
from pages.views import home_view,contact_view, home_view1,about_view
from products.views import product_detail_view, product_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home_view, name='home'),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('home1/', home_view1, name='home1'),
    path('about/', about_view, name='about'),
    path('product/', product_detail_view),
    path('create/', product_create_view),
]
