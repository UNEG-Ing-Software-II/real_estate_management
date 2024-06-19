from django.urls import path
from app_Principal.views import *
from app_Principal.Controladores.InmuebleController import *
from app_Principal.Controladores.usuariosController import *
from app_Principal.Controladores.areasController import *


urlpatterns = [
    path('',index,name='index'),
    path('login', login_view, name = 'login'),
    path('inicio_coordinador',coordinador, name='inicio Coordinador' ),
    path('inicio_asesor',asesor, name='inicio Asesor'),
    path('inicio_director_general',director_general, name='inicio Director General'),

    path('cerrar_sesion',cerrar_sesion, name='cerrar sesion'),
    path('crear_usuario',crear_usuario, name='crear usuario'),
    path('cuenta_usuario',cuenta_usuario, name='cuenta usuario'),
    #inmuebles
    path('detalles-inmueble/<uuid:inmueble_id>/', detalles_inmueble, name='inmueble_detalles'), #URL de vista para modificar/eliminar inmmueble
    path('inmuebles-registrados/', inmuebles_registrados, name='inmuebles registrados'), #Leer
    path('registrar-inmueble/', registrar_inmueble, name='registrar_inmueble'), #Crear
    path('modificar_inmueble/<uuid:inmueble_id>/', modificar_inmueble, name='modificar_inmueble'),
    path('eliminar_inmueble/<uuid:inmueble_id>/', eliminar_inmueble, name='eliminar_inmueble'),
    #Procesos con los usuarios propietarios
    path('buscar_propietario/', buscar_propietario, name='buscar_propietario'),
    path('validar_propietario_nuevo', validar_propietario, name='validar_propietario'),
    path('guardar_propietario_inmueble/', guardar_propietario_inmueble, name='guardar_propietario'),
    path('eliminar_propietarios',eliminar_propietarios, name='eliminar_propietarios'),
    #Areas
    path('registrar_area',registrar_area, name='registrar_area'),
    path('eliminar_area/<uuid:area_id>', eliminar_area, name="eliminar_area"),
    path('modificar_area/<uuid:area_id>', modificar_area, name="modificar_area"),
    #script de areas
    path('scrip_llenado_caracteristicas',scrip_llenado_caracteristicas, name="scrip_llenado_caracteristicas")
]
