"""hellowrld_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import hello.views
import hello1.views
import hello2.views
import hello3.views
import hello4.views
import hello5.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello.views.home, name ='home'),
    path('home1', hello1.views.home1, name ='home1'),
    path('home2', hello2.views.home2, name ='home2'),
    path('home3', hello3.views.home3, name ='home3'),
    path('home4', hello4.views.home4, name ='home4'),
    path('home5', hello5.views.home5, name ='home5'),
]