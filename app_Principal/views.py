from django.shortcuts import render, redirect
from app_Principal.models import *
from django.http import request
from MyR.backend import *  # importancion para funciones de la carpeta backend.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # importacion para mensajes de error
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import update_session_auth_hash

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
    imagenes_inmueble = Imagen_inmueble.objects.filter(inmueble=inmueble)
    incidencia = Incidencia.objects.all()    
    incidenciaRelacion = Relacion_incidencia.objects.filter( inmueble=inmueble_id)
    asesor = Usuario.objects.filter(rol='Asesor')
    context = {
        'inmueble': inmueble,
        'imagenes_inmueble': imagenes_inmueble,
        'incidencias': incidencia,
        'incidenciaRelacion':incidenciaRelacion,
        'asesores':asesor,
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




# ---------------------------------------------------------------


@login_required(login_url='login')
def cuenta_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        cedula_nueva = request.POST.get('cedula')
        nombre_nuevo = request.POST.get('nombre')
        apellido_nuevo = request.POST.get('apellido')
        correo_nuevo = request.POST.get('correo')
        password_nueva = request.POST.get('password')

        # Verificar y actualizar los datos del usuario
        '''if cedula_nueva:
            if Usuario.objects.exclude(pk=usuario.pk).filter(cedula=cedula_nueva).exists():
                messages.error(request, 'Esta cédula ya está en uso por otro usuario.')
                return redirect('cuenta usuario')
            else:
                usuario.cedula = cedula_nueva'''
        if nombre_nuevo:
            usuario.nombre = nombre_nuevo
        if apellido_nuevo:
            usuario.apellido = apellido_nuevo
        if correo_nuevo:
            if Usuario.objects.exclude(pk=usuario.pk).filter(correo=correo_nuevo).exists():
                messages.error(request, 'Este correo ya está en uso por otro usuario.')
                return redirect('cuenta usuario')
            else:
                usuario.correo = correo_nuevo
        if password_nueva:
            usuario.set_password(password_nueva)

        usuario.save()
        messages.success(request, 'Datos actualizados correctamente.')
        return redirect('cuenta usuario')
    else:
        # Pasar el usuario al contexto si no hay una solicitud POST
        return render(request, 'datos_cuenta.html', {'usuario': usuario})


"""
# ESTO BORRA TODAS LAS TABLAS DEL RAILWAY Y LOCAL, USAR CUANDO SE ACTUALICE LA BD
from django.db import connection

def eliminar_todas_las_tablas():
    with connection.cursor() as cursor:

        cursor.execute('SET session_replication_role = replica;')
        cursor.execute('DROP SCHEMA public CASCADE; CREATE SCHEMA public;')
        cursor.execute('SET session_replication_role = DEFAULT;')

    print("Todas las tablas han sido eliminadas, incluyendo aquellas con restricciones de clave externa.")

eliminar_todas_las_tablas()
"""