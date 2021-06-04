from django.urls import path
from . import views

urlpatterns = [
    path('createPlayer/', views.createPlayerView, name="create-player-view"),
    path('viewPlayers/', views.playersView,name="players-view"),
    path('createTeam/<int:n>', views.createTeamView,name="create-team-view"),
]