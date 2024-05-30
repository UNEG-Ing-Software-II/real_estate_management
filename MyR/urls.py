"""
URL configuration for MyR project.

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
from app_Principal.views import *
#from MyR.backend import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('',index,name='index'),
    path('login', login_view, name = 'login'),
    path('inicio_coordinador',coordinador, name='inicio Coordinador' ),
    path('inicio_asesor',asesor, name='inicio Asesor' ),
    path('inicio_director_general',director_general, name='inicio Director General'),
    path('cerrar_sesion',cerrar_sesion, name='cerrar sesion'),
    path('crear_usuario',crear_usuario, name='crear usuario')
]