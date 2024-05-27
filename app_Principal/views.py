
from django.shortcuts import render, redirect
from app_Principal.models import *
from django.http import request
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    #usuario = CustomUser.objects.get(rol='Director')
    user = authenticate(correo='prjr2003@gmail.com',password='password')
    if user is not None:
        print("usuario: ",user)
        login(request, user)
        logueado = request.user
        print("rol del usuario logueado: ",logueado.rol,logueado.password,logueado.nombre,logueado.apellido) 

    else:
        print("no hay na pa")    



    return render(request, "index.html")    





    