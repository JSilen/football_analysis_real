from django.shortcuts import render, redirect
from .models import Player, Match, Performance
from django.contrib.auth.decorators import login_required
from .forms import PlayerForm, MatchForm, PerformanceForm

def index(request):
    return render(request, 'football_app/index.html')

def players(request):
    players = Player.objects.order_by('name')
    context = {'players':players}
    return render(request, 'football_app/players.html', context)

def matches(request):
    matches = Match.objects.order_by('date')
    context = {'matches':matches}
    return render(request, 'football_app/matches.html', context)

def performances(request):
    performances = Performance.objects.order_by('match')
    context = {'performances':performances}
    return render(request, 'football_app/performances.html', context)

def player(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'football_app/player.html', {'player': player})

def match(request, match_id):
    match = Match.objects.get(id=match_id)
    return render(request, 'football_app/match.html', {'match': match})

def performance(request, performance_id):
    performance = Performance.objects.get(id=performance_id)
    return render(request, 'football_app/performance.html', {'performance':performance})

def add_player(request):
    if request.method != 'POST':
        form = PlayerForm()
    else:
        form = PlayerForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('football_app:players')
    context = {'form':form}
    return render(request, 'football_app/add_player.html', context)

def add_match(request):
    if request.method != 'POST':
        form = MatchForm()
    else:
        form = MatchForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('football_app:matches')
    context = {'form':form}
    return render(request, 'football_app/add_match.html', context)

def add_performance(request):
    if request.method != 'POST':
        form = PerformanceForm()
    else:
        form = PerformanceForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('football_app:performances')
    context = {'form':form}
    return render(request, 'football_app/add_performance.html', context)