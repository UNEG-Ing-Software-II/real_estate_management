from django.urls import path
from app_Principal.views import *
from app_Principal.Controladores.InmuebleController import *


urlpatterns = [
    path('',index,name='index'),
    path('login', login_view, name = 'login'),
    path('inicio_coordinador',coordinador, name='inicio Coordinador' ),
    path('inicio_asesor',asesor, name='inicio Asesor'),
    path('inicio_director_general',director_general, name='inicio Director General'),
    path('cerrar_sesion',cerrar_sesion, name='cerrar sesion'),
    path('crear_usuario',crear_usuario, name='crear usuario'),
    #inmuebles
    path('inmuebles-registrados/', inmuebles_registrados, name='inmuebles registrados'), #Leer
    path('registrar-inmueble/', registrar_inmueble, name='registrar_inmueble'), #Crear
    path('modificar_inmueble/<uuid:inmueble_id>/', modificar_inmueble, name='modificar_inmueble'),
    path('eliminar_inmueble/<uuid:inmueble_id>/', eliminar_inmueble, name='eliminar_inmueble'),
]
