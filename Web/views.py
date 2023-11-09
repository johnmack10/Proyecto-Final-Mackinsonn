from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario, fechas: {hoy.day}/{hoy.month}"
    respuesta_html = HttpResponse(saludo)
    return respuesta_html


def saludar_con_html(request):
    contexto = {}
    
    http_Response = render( 
        request=request,
        template_name="inicio.html",
        context=contexto,
    )

    return http_Response
