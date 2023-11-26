from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def presentacion(request):
    contexto = {}
    
    http_Response = render( 
        request=request,
        template_name="presentacion.html",
        context=contexto,
    )

    return http_Response


def saludar_con_html(request):
    contexto = {}
    
    http_Response = render( 
        request=request,
        template_name="inicio.html",
        context=contexto,
    )

    return http_Response
