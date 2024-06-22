from django import forms
from app.models import *
from django.contrib.auth.decorators import login_required
from MyR.backend import role_required     
from django.shortcuts import render, redirect, get_object_or_404

@login_required(login_url='login')
@role_required('Asesor')
def agregar_incidencia(request, inmueble_id):
    if request.method == "POST":
        incidencia = Relacion_incidencia(
            inmueble= inmueble_id,
            asesor=request.POST["asesor"],
            nombre=request.POST["nombre"],
            tipo=request.POST["tipo"],
            

                                
        )
        return redirect('inicio Asesor')

    return redirect('inicio Asesor')

    