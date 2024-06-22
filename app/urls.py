from django.urls import path
from app import views
from app.controllers.UserController import UserController
from app.controllers.EstateController import EstateController
# from app.controllers.areasController import *


urlpatterns = [
    path('',views.home,name='home'),
    path('login', views.sign_in, name = 'login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_off', views.sign_off, name='sign_off'),
    path('my_account',views.my_account, name='my_account'),

    # #Estate
    path("estate/<int:estate_id>/", EstateController.read, name="estate"), #URL view to modify/eliminate property
    path("estate/create", EstateController.create, name="estate_create"),
    path("estate/update", EstateController.update, name="estate_update"),
    path("estate/delete", EstateController.delete, name="estate_delete"),

    #User
    path("save_owner", UserController.save_owner, name="save_owner"),
    path("unlink_owner", UserController.unlink_owner, name="unlink_owner"),
    path("search_owner", UserController.search_owner, name="search_owner"),
    path("validate_owner", UserController.validate_owner, name="validate_owner")

    # path('inmuebles-registrados/', inmuebles_registrados, name='inmuebles registrados'), #Leer
    # path('registrar-inmueble/', registrar_inmueble, name='registrar_inmueble'), #Crear
    # path('modificar_inmueble/<uuid:inmueble_id>/', modificar_inmueble, name='modificar_inmueble'),
    # path('eliminar_inmueble/<uuid:inmueble_id>/', eliminar_inmueble, name='eliminar_inmueble'),
    # #Procesos con los usuarios propietarios
    # path('buscar_propietario/', buscar_propietario, name='buscar_propietario'),
    # path('validar_propietario_nuevo', validar_propietario, name='validar_propietario'),
    # path('guardar_propietario_inmueble/', guardar_propietario_inmueble, name='guardar_propietario'),
    # path('eliminar_propietarios',eliminar_propietarios, name='eliminar_propietarios'),
    # #Areas
    # path('registrar_area',registrar_area, name='registrar_area'),
    # path('eliminar_area/<uuid:area_id>', eliminar_area, name="eliminar_area"),
    # path('modificar_area/<uuid:area_id>', modificar_area, name="modificar_area"),
    # #script de areas
    # path('scrip_llenado_caracteristicas',scrip_llenado_caracteristicas, name="scrip_llenado_caracteristicas")
]
