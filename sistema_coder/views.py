from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario"
    respuesta_html = HttpResponse(saludo)
    return  respuesta_html

def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"hola querido usuario, fecha {hoy.day}/{hoy.month}"
    respuesta_html = HttpResponse(saludo)
    return  respuesta_html



def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response


