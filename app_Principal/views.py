
from django.shortcuts import render, redirect
from app_Principal.models import *
from django.http import request
from MyR.backend import * #importancion para funciones de la carpeta backend.py
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages #importacion para mensajes de error

# Create your views here.

#funcion para procesar el inicio de sesion
def index(request):
    if request.user.is_authenticated: #verificamos primero si en el computador  hay un usario logueado
        messages.error(request, 'usted ya esta logueado.', extra_tags='access_denied')
        User = request.user
        return redirecion(User.rol)  # llama a la funcion redirecion que se encuentra en el archivo backend.py y determina su inicio dependiendo el rol
   
    next_page = request.GET.get('next')

    if request.method == "POST": #si el usuario no esta logueado, se recibe las credenciales y se procesan
        correo = request.POST["correo"]
        password = request.POST["password"]
        user = authenticate(correo=correo, password=password)

        if user is not None:
            login(request, user)
            print("usuario: ",user)

            if next_page:
                return redirect(next_page)  # Redirigir al usuario a la página 'next' después de iniciar sesión (osea la pagina que intento visitar antes)
            else:
                return redirecion(user.rol)  # llama a la funcion redirecion que se encuentra en el archivo backend.py y determina su inicio dependiendo el rol
        else:
            guardar_usuario()
            error_message = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
            return render(request, 'index.html', {'error_message': error_message}) #vuelva a llamar al inicio de login y manda el mensaje de error

    return render(request, 'index.html', {'next_page': next_page})

def coordinador(request):
   
    return render(request,'inicio_coordinador.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('index')
