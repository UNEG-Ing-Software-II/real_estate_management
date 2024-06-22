from django import forms
from app.models import *
from django.contrib.auth.decorators import login_required
from MyR.backend import role_required
from django.shortcuts import render, redirect, get_object_or_404


class TaskController:

    @login_required(login_url='login')
    def create(request):
        if request.method != "POST":
            return redirect("home")

        data = {
            "estate_id": Estate.objects.get(pk=request.POST.get("estate_id")),
            "consultant_id": User.objects.get(pk=request.POST.get("consultant_id")),
            "task_id": Task.objects.get(pk=request.POST.get("task_id")),
            "done": True if request.POST.get("done") else False
        }

        EstateTask.objects.create(**data)

        return redirect("estate", estate_id=request.POST.get("estate_id"))
