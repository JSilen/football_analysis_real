from django import forms
from .models import Player, Match, Performance

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 
                  'age', 
                  'position', 
                  'pref_foot', 
                  'nationality', 
                  'team',
        ]

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = [
            'date', 
            'home_team', 
            'away_team', 
            'competition', 
            'goals_for', 
            'goals_against',         
        ]
        
class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = [
            'player',
            'match',
            'minutes',
            'goals',
            'assists',
            'shots',
            'shots_on_goals',
            'total_passes',
            'passes_completed',
            'xg',
            'yellow_cards',
            'red_cards',
        ]