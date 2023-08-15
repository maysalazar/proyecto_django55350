from django.shortcuts import render, redirect
from django.urls import reverse

from control_estudios.models import Curso, Estudiante


def listar_estudiantes(request):
    contexto = {
        "profesor": "pedro",
        "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response


def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
        
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response


def crear_curso(request):
   if request.method == "POST":
       data = request.POST
       nombre = data['nombre']
       comision = data['comision']
       curso = Curso(nombre=nombre, comision=comision)
       curso.save()
       
       url_exitosa = reverse('lista_cursos')
       return redirect(url_exitosa)
   else:  # GET
       http_response = render(
           request=request,
           template_name='control_estudio/formulario_curso_a_mano.html',
       )
       return http_response

