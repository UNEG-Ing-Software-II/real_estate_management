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
    return render(request, "views_asesor/views_asesor.html")

@login_required(login_url='login')
@role_required('Director General')
def director_general(request):
    return render(request, "inicio_DG.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("login")

# -------------------------------------------------------------------------------------#
# CRUD para los inmuebles


# Leer inmuebles
def read_inmueble(request):
    if request.method == "GET":
        # Consulta a la tabla Inmueble para obtener todos los registros
        # inmueble = Inmueble.objects.all()

        # Pasar los datos al contexto de renderizado
        # context = {"inmuebles": inmueble}

        return render(
            request, "read_inmueble.html", {"inmuebles": Inmueble.objects.all()}
        )


# Crear inmueble
def create_inmueble(request):
    if request.method == "GET":
        # usuario = Usuario.objects.all()
        # context = {"usuario": usuario}
        return render(
            request, "create_inmueble.html", {"usuario": Usuario.objects.all()}
        )

    values = get_inmueble_values(request.POST)
    Inmueble.objects.create(**values)

    # propietario_id = request.POST["propietario_id"]
    # precio = request.POST["precio"]
    # tipoPropiedad =  request.POST["tipoPropiedad"]
    # niveles =  request.POST["niveles"]
    # metros_terreno = request.POST["metros_terreno"]
    # metros_construccion = request.POST["metros_construccion"]
    # bathroom = request.POST["bathroom"]
    # cuarto_servicio = request.POST["cuarto_servicio"]
    # oficina = request.POST["oficina"]
    # estacionamiento = request.POST["estacionamiento"]
    # half_bath = request.POST["half_bath"]
    # terraza = request.POST["terraza"]
    # habitacion = request.POST["habitacion"]
    # maletero = request.POST["maletero"]

    # Inmueble.objects.create(propietario_id = propietario_id , precio = precio, tipoPropiedad = tipoPropiedad,
    #                         niveles = niveles, metros_terreno = metros_terreno, metros_construccion = metros_construccion,
    #                         bathroom = bathroom, cuarto_servicio = cuarto_servicio, oficina = oficina, estacionamiento = estacionamiento,
    #                         half_bath = half_bath, terraza = terraza, habitacion = habitacion, maletero = maletero)

    # return redirect("/view_director_g/create_inmueble")


# Modificar inmueble


def update_inmueble(request):
    if request.method == "GET":
        inmueble = Inmueble.objects.all()
        usuario = Usuario.objects.all()
        context = {"inmuebles": inmueble, "usuario": usuario}
        return render(request, "update_inmueble.html", context)

    vals = get_inmueble_values(request.POST)
    # # Obtener los datos actualizados del formulario
    # # inmueble_id = request.POST["inmueble"]
    # propietario_id = request.POST["propietario_id"]
    # precio = request.POST["precio"]
    # tipoPropiedad =  request.POST["tipoPropiedad"]
    # niveles =  request.POST["niveles"]
    # metros_terreno = request.POST["metros_terreno"]
    # metros_construccion = request.POST["metros_construccion"]
    # bathroom = request.POST["bathroom"]
    # cuarto_servicio = request.POST["cuarto_servicio"]
    # oficina = request.POST["oficina"]
    # estacionamiento = request.POST["estacionamiento"]
    # half_bath = request.POST["half_bath"]
    # terraza = request.POST["terraza"]
    # habitacion = request.POST["habitacion"]
    # maletero = request.POST["maletero"]

    inmueble = get_object_or_404(Inmueble, pk=request.POST["inmueble"])

    # Actualizar los campos del inmueble
    inmueble.propietario_id = vals["propietario_id"]
    inmueble.precio = vals["precio"]
    inmueble.tipoPropiedad = vals["tipoPropiedad"]
    inmueble.niveles = vals["niveles"]
    inmueble.metros_terreno = vals["metros_terreno"]
    inmueble.metros_contruccion = vals["metros_construccion"]
    inmueble.bathroom = vals["bathroom"]
    inmueble.cuarto_servicio = vals["cuarto_servicio"]
    inmueble.oficina = vals["oficina"]
    inmueble.estacionamiento = vals["estacionamiento"]
    inmueble.half_bath = vals["half_bath"]
    inmueble.terraza = vals["terraza"]
    inmueble.habitacion = vals["habitacion"]
    inmueble.maletero = vals["maletero"]

    # Guardar los cambios en la base de datos
    inmueble.save()
    return redirect("/view_director_g/update_inmueble/")


def delete_inmueble(request):
    if request.method == "GET":
        # inmueble = Inmueble.objects.all()
        # Pasar los datos al contexto de renderizado
        # context = {"inmueble": inmueble}
        return render(
            request,
            "delete_edificio.html",
            {"inmueble": Inmueble.objects.all()},
        )

    inmueble = get_object_or_404(Inmueble, pk=request.POST["inmueble"])
    # Eliminar el condominio
    inmueble.delete()
    return redirect("/view_director_g/delete_inmueble/")


@login_required(login_url='login')
@role_required('Asesor')
def inmueble(request, inmueble_id):
    context = {
        'inmueble_id':inmueble_id 
    }
    return render(request, 'views_asesor/inmueble.html', context)
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
