from app.models import *
from django.shortcuts import redirect, render
from app.models import *
from django.http import request
from functools import wraps
from django.http import HttpResponseForbidden


# Esta funcion recibe el rol del usuario que esta logueado, dependiendo lo va a redirigir a su pagina correspondiente
# obviamente va a dar error porque ninguna de las paginas estan predefinidas en el archivo urls.py
# basicamente cada return va llamar a la funcion del archivo views.py que procesa cada vista, claro la direccion debe estar en el archivo urls.py
def redirecion(rol):
    roles = {
        "Director General": "Director General",
        "Coordinador": "Coordinador",
        "Asesor": "Asesor",
        "Propietario": "Propietario",
    }
    return redirect("inicio %s" % roles.get(rol))


def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")
            if request.user.rol != role:
                # return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
                return redirecion(request.user.rol)
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


    # if rol=="Director General":
    #     print("usted entro en la vista Director general")
    #     return redirect("inicio director_General")
    # elif rol=="Coordinador":
    #     print("usted entro en la vista Coordinador")
    #     return redirect("inicio Coordinador")
    # elif rol=="Asesor":
    #     print("usted entro en la vista Asesor")
    #     #return redirect("inicio Asesor")
    # elif rol=="Propietario":
    #     print("usted entro en la vista Propietario")
    #     return redirect("inicio Propietario")


# funcion temporal para cargar un registro a la tabla usuario

def guardar_usuario():
    Usuario.objects.create_user(
        cedula="123456789",
        password="admin",
        nombre="Admin",
        apellido="Admin",
        rol="Asesor",
        correo="admin@gmail.com",
    )


def get_inmueble_values(vals):
    return {
        "propietario_id": vals["propietario_id"],
        "precio": vals["precio"],
        "tipoPropiedad": vals["tipoPropiedad"],
        "niveles": vals["niveles"],
        "metros_terreno": vals["metros_terreno"],
        "metros_construccion": vals["metros_construccion"],
        "bathroom": vals["bathroom"],
        "cuarto_servicio": vals["cuarto_servicio"],
        "oficina": vals["oficina"],
        "estacionamiento": vals["estacionamiento"],
        "half_bath": vals["half_bath"],
        "terraza": vals["terraza"],
        "habitacion": vals["habitacion"],
        "maletero": vals["maletero"],
    }
