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
    path('editar_remera/<int:id>/', editar_remera, name='editar_remera'),
    path('borrar_remera/<int:id>/', borrar_remera, name='borrar_remera'),
    path('remeras/find/', search_remeras, name="search_remeras"),
    path('calzado/', ver_calzado),
    path('post_calzado/', post_calzado, name='post_calzado'),
    path('editar_calzado/<int:id>/', editar_calzado, name='editar_calzado'),
    path('borrar_calzado/<int:id>/', borrar_calzado, name='borrar_calzado'),
    path('calzado/find/', search_calzado, name="search_calzado"),
    path('gorras/', ver_gorras),
    path('post_gorras/', post_gorras, name='post_gorras'),
    path('editar_gorras/<int:id>/', editar_gorra, name='editar_gorra'),
    path('borrar_gorra/<int:id>/', borrar_gorra, name='borrar_gorra'),
    path('gorras/find/', search_gorras, name="search_gorras"),
    path("login/", login_request, name="login"),
    path('register/', register, name='register'),
    path("logout/", logout_view, name="logout")
]
