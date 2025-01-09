from django.urls import path
from . import views

app_name = 'football_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('players/', views.players, name='players'),
    path('players/<int:player_id>/', views.player, name='player'),
    path('matches/', views.matches, name='matches'),
    path('matches/<int:match_id>/', views.match, name='match'),
    path('performances/', views.performances, name='performances'),
    path('performances/<int:performance_id>/', views.performance, name='performance'),
    path('add-player/', views.add_player, name='add_player'),
    path('add-match/', views.add_match, name='add_match'),
    path('add-performance/', views.add_performance, name='add_performance'),
]