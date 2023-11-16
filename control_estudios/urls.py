from django.contrib import admin
from django.urls import path

from control_estudios.views import (listar_torneos, ingresar_torneo, buscar_torneos,listar_jugadores,ingresar_jugador,buscar_jugadores,
                                    eliminar_torneo,editar_torneo,RankingListView,RankingDetailView,RankingCreateView,RankingUpdateView,RankingDeleteView)

urlpatterns = [
    path("Torneos/", listar_torneos, name ="listar_torneos"),
    path("Nuevo-Torneo/", ingresar_torneo, name = "ingresar_torneo"),
    path("Buscar-Torneo/", buscar_torneos, name="buscar_torneos"),
    path("Jugadores/", listar_jugadores, name="listar_jugadores"),
    path("Nuevo-Jugador/", ingresar_jugador, name="ingresar_jugador"),
    path("Buscar-jugador/", buscar_jugadores, name="buscar_jugadores"),
    path('Eliminar-Torneo/<int:id>/', eliminar_torneo, name="eliminar_torneo"),
    path('Editar-Torneo/<int:id>/', editar_torneo, name="editar_torneo"),
    path("Ranking/", RankingListView.as_view(), name="lista_ranking"),
    path('Ranking/<int:pk>/', RankingDetailView.as_view(), name="ver_ranking"),
    path('crear-Ranking/', RankingCreateView.as_view(), name="crear_ranking"),
    path('editar-Ranking/<int:pk>/', RankingUpdateView.as_view(), name="editar_ranking"),
    path('eliminar-Ranking/<int:pk>/', RankingDeleteView.as_view(), name="eliminar_ranking"),
    
]

