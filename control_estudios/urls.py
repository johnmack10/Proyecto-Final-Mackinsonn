from django.contrib import admin
from django.urls import path

from control_estudios.views import (listar_torneos, ingresar_torneo, buscar_torneos,listar_jugadores,ingresar_jugador,buscar_jugadores,ingresar_al_ranking,listar_ranking)

urlpatterns = [
    path("Torneos/", listar_torneos, name ="listar_torneos"),
    path("Nuevo-Torneo/", ingresar_torneo, name = "ingresar_torneo"),
    path("Buscar-Torneo/", buscar_torneos, name="buscar_torneos"),
    path("Jugadores/", listar_jugadores, name="listar_jugadores"),
    path("Nuevo-Jugador/", ingresar_jugador, name="ingresar_jugador"),
    path("Buscar-jugador/", buscar_jugadores, name="buscar_jugadores"),
    path("Nuevo-Ranking/", ingresar_al_ranking, name="ingresar_al_ranking"),
    path("Ranking/", listar_ranking, name="listar_ranking"),
    
]

