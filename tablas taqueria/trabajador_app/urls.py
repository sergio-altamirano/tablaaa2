from django.urls import path
from trabajador_app import views

urlpatterns = [
    path('',views.inicio_vista,name="inicio_vista"),
    path("registrarTrabajador/",views.registrarTrabajador,name="registrarTrabajador")
]