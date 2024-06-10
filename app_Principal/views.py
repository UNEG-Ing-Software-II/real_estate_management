from django.shortcuts import render, redirect
from app_Principal.models import *
from django.http import request
from MyR.backend import *  # importancion para funciones de la carpeta backend.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # importacion para mensajes de error
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index(request):
    return render(request, "index.html")

# funcion para procesar el inicio de sesion
def login_view(request):
    # Verificamos primero si en el computador  hay un usario logueado
    if request.user.is_authenticated:
        messages.error(
            request, "usted ya esta logueado.", extra_tags="access_denied"
        )

        # Llama a la funcion redirecion que se encuentra en el archivo backend.py y determina su inicio dependiendo el rol
        return redirecion(request.user.rol)

    next_page = request.GET.get("next")

    # Si el usuario no esta logueado, se recibe las credenciales y se procesan
    if request.method == "POST":
        user = authenticate(
            correo=request.POST["correo"], password=request.POST["password"]
        )

        if user is not None:
            login(request, user)
            print("usuario: ", user)

            # Redirigir al usuario a la página "next" después de iniciar sesión (osea la pagina que intento visitar antes)
            if next_page:
                return redirect(next_page)

            return redirecion(
                user.rol
            )  # Llama a la funcion redirecion que se encuentra en el archivo backend.py y determina su inicio dependiendo el rol

        #guardar_usuario()
        return render(
            request,
            "login.html",
            {
                "error_message": "Credenciales inválidas. Por favor, inténtalo de nuevo."
            },
        )  # vuelva a llamar al inicio de login y manda el mensaje de error

    return render(request, "login.html", {"next_page": next_page})

@login_required(login_url='login')
@role_required('Coordinador')
def coordinador(request):
    return render(request, "inicio_coordinador.html")

@login_required(login_url='login')
@role_required('Asesor')
def asesor(request):
    inmuebles = Inmueble.objects.all()
    return render(request, "views_asesor/views_asesor.html", {'inmuebles': inmuebles})

@login_required(login_url='login')
@role_required('Director General')
def director_general(request):
    return render(request, "inicio_DG.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
@role_required('Asesor')
def detalles_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    context = {
        'inmueble': inmueble 
    }
    return render(request, 'views_asesor/inmueble_detalle.html', context)

# -------------------------------------------------------------------------------------#
# Crear usuario (provisional)

def crear_usuario(request):
    if request.method == "POST":
        Usuario.objects.create_user(
            cedula=request.POST["cedula"],
            correo=request.POST["correo"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            password=request.POST["password"],
            rol=request.POST["rol"],
        )
        print("usuario registrado correctamente")
        return render(request, "index.html")
    return render(request,"registrar_usuario.html")



# ESTO BORRA TODAS LAS TABLAS DEL RAILWAY, USAR CUANDO SE ACTUALICE LA BDcls
# from django.db import connection

# def eliminar_todas_las_tablas():
#     with connection.cursor() as cursor:

#         cursor.execute('SET session_replication_role = replica;')
#         cursor.execute('DROP SCHEMA public CASCADE; CREATE SCHEMA public;')
#         cursor.execute('SET session_replication_role = DEFAULT;')

#     print("Todas las tablas han sido eliminadas, incluyendo aquellas con restricciones de clave externa.")

# eliminar_todas_las_tablas()