from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control_estudios.models import Jugador,Ranking, Torneo
from control_estudios.forms import Torneoformulario,Jugadorformulario, Rankingformulario

def listar_torneos(request):
    contexto = {
    "torneos": Torneo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_torneos.html',
        context=contexto,
    )
    return http_response



def ingresar_torneo(request):
   if request.method == "POST":
       formulario = Torneoformulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           nombre = data["nombre_torneo"]
           comision = data["fecha_comienzo"]
           curso = Torneo(nombre_torneo=nombre, fecha_comienzo=comision)  
           curso.save()  

           url_exitosa = reverse('listar_torneos')  
           return redirect(url_exitosa)
   else:  
       formulario = Torneoformulario()
   http_response = render(
       request=request,
       template_name='control_estudios/formulario_torneo.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_torneos(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       torneos = Torneo.objects.filter(
            Q(nombre_torneo__icontains=busqueda) | Q(fecha_comienzo__contains=busqueda)
        )
       contexto = {
           "torneos": torneos,
       }
       http_response = render(
           request=request,
           template_name='control_estudios/lista_torneos.html',
           context=contexto,
       )
       return http_response
   
def listar_jugadores(request):
    contexto = {
    "jugadores": Jugador.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_jugadores.html',
        context=contexto,
    )
    return http_response

def ingresar_jugador(request):
   if request.method == "POST":
       formulario = Jugadorformulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           nombre = data["nombre"]
           apellido = data["apellido"]
           nacimiento = data["fecha_nacimiento"]
           telefono = data["telefono"]
           curso = Jugador(nombre=nombre, apellido=apellido, fecha_nacimiento=nacimiento,telefono=telefono) 
           curso.save()  

           url_exitosa = reverse('listar_jugadores')  
           return redirect(url_exitosa)
   else:  
       formulario = Jugadorformulario()
   http_response = render(
       request=request,
       template_name='control_estudios/formulario_jugador.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_jugadores(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       jugadores = Jugador.objects.filter(
            Q(nombre__icontains=busqueda) | Q(apellido__contains=busqueda)
        )
       contexto = {
           "jugadores": jugadores,
       }
       http_response = render(
           request=request,
           template_name='control_estudios/lista_jugadores.html',
           context=contexto,
       )
       return http_response
   
def listar_ranking(request):
    contexto = {
    "ranking": Ranking.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_ranking.html',
        context=contexto,
    )
    return http_response

def ingresar_al_ranking(request):
   if request.method == "POST":
       formulario = Rankingformulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  
           nombre = data["nombre"]
           puntos = data["cantidad_puntos"]
           torneos = data["torneos_jugados"]
           apellido = data["apellido"]
           ranking = Ranking(nombre=nombre, cantidad_puntos=puntos, torneos_jugados = torneos, apellido=apellido)  
           ranking.save()  
           url_exitosa = reverse('listar_ranking')  
           return redirect(url_exitosa)
   else:  
       formulario = Rankingformulario()
   http_response = render(
       request=request,
       template_name='control_estudios/formulario_ranking.html',
       context={'formulario': formulario}
   )
   return http_response