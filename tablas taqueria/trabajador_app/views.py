from django.shortcuts import render,redirect
from .models import Trabajador

# Create your views here.

def inicio_vista(request):
    lostrabajadores=Trabajador.objects.all()
    return render(request,'gestionarTrabajador.html',{"mistrabajadores":lostrabajadores})

def registrarTrabajadores(request):
    id_trabajador=request.POST["txtid_trabajador"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    puesto=request.POST["txtpuesto"]
    fecha_nacimiento=request.POST["txtfecha"]
    curp=request.POST["txtcurp"]
    salario=request.POST["numsalario"]

    guardarmateria=Trabajador.objects.create(id_trabajador=id_trabajador,nombre=nombre,apellido=apellido,puesto=puesto,fecha_nacimiento=fecha_nacimiento,curp=curp,salario=salario) 

    return redirect('/')