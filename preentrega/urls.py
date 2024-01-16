"""
URL configuration for preentrega project.

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
from django.urls import path
from proyectocoder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio),
    path('remeras/', ver_remeras),
    path('post_remeras/', post_remeras, name='post_remeras'),
    path('remeras/find/', search_remeras, name="search_remeras"),
    path('calzado/', ver_calzado),
    path('post_calzado/', post_calzado, name='post_calzado'),
    path('calzado/find/', search_calzado, name="search_calzado"),
    path('gorras/', ver_gorras),
    path('post_gorras/', post_gorras, name='post_gorras'),
    path('gorras/find/', search_gorras, name="search_gorras"),
]
