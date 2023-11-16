from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView

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
           template_name='control_estudios/lista_jugadores.html',
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
   
def eliminar_torneo(request, id):
   torneo = Torneo.objects.get(id=id)
   if request.method == "POST":
       torneo.delete()
       url_exitosa = reverse('listar_torneos')
       return redirect(url_exitosa)
   

def editar_torneo(request, id):
   torneo = Torneo.objects.get(id=id)
   if request.method == "POST":
       formulario = Torneoformulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           torneo.nombre_torneo = data['nombre_torneo']
           torneo.fecha_comienzo = data['fecha_comienzo']
           torneo.save()
           url_exitosa = reverse('listar_torneos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': torneo.nombre_torneo,
           'fecha': torneo.fecha_comienzo,
       }
       formulario = Torneoformulario(initial=inicial)
   return render(
       request=request,
       template_name='control_estudios/formulario_torneo.html',
       context={'formulario': formulario},
   )

class RankingListView(ListView):
   model = Ranking
   template_name = 'control_estudios/lista_ranking.html'
   def get_queryset(self):
        queryset = super().get_queryset()
        return sorted(queryset, key=lambda ranking: ranking.cantidad_puntos, reverse=True)
class RankingCreateView(CreateView):
   model = Ranking
   fields = ('apellido', 'nombre', 'cantidad_puntos', 'torneos_jugados')
   success_url = reverse_lazy('lista_ranking')
   
class RankingDetailView(DetailView):
   model = Ranking
   success_url = reverse_lazy('lista_ranking')
   
class RankingUpdateView(UpdateView):
   model = Ranking
   fields = ('apellido', 'nombre', 'cantidad_puntos', 'torneos_jugados')
   success_url = reverse_lazy('lista_ranking')
class RankingDeleteView(DeleteView):
   model = Ranking
   success_url = reverse_lazy('lista_ranking')