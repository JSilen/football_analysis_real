from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(default="Insert age...", max_length=10)
    position = models.CharField(max_length=30, choices=[
        ('GK', 'Goalkeeper'),
        ('LB', 'Left Back'),
        ('RB', 'Right Back'),
        ('LWB', 'Left Wing Back'),
        ('RWB', 'Right Wing Back'),
        ('CB', 'Center Back'),
        ('CDM', 'Central Defensive Midfielder'),
        ('CM', 'Central Midfielder'),
        ('CAM', 'Central Attacking Midfielder'),
        ('LW', 'Left Winger'),
        ('RW', 'Right Winger'),
        ('ST', 'Striker'),
    ])
    pref_foot = models.CharField(max_length=10, choices=[
        ('R', 'Right'),
        ('L', 'Left'),
    ])
    nationality = models.CharField(max_length=200, default="Select nationality...")
    team = models.CharField(max_length=200, default="Select team...")

    def __str__(self):
        return f"{self.name}, {self.position}, {self.team}"


class Match(models.Model):
    date = models.DateField(null=True, blank=True)
    home_team = models.CharField(max_length=200, blank=False)
    away_team = models.CharField(max_length=200, blank=False)
    competition = models.CharField(max_length=200, blank=False)
    goals_for = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.home_team} vs. {self.away_team}, {self.date}"


class Performance(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    minutes = models.PositiveIntegerField(default=0)
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    shots = models.PositiveIntegerField(default=0)
    shots_on_goals = models.PositiveIntegerField(default=0)
    total_passes = models.PositiveIntegerField(default=0)
    passes_completed = models.PositiveIntegerField(default=0)
    xg = models.FloatField(default=0.0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)
    
    def shot_percentage(self):
        if self.shots > 0:
            return f"{(self.shots_on_goals / self.shots) * 100:.2f} %"
        return "0.00 %"
    
    def pass_accuracy(self):
        if self.total_passes > 0:
            return f"{(self.passes_completed / self.total_passes) * 100:.2f} %"
        return "0.00 %"
    
    def minutes_per_goal(self):
        if self.goals > 0:
            return f"{self.minutes / self.goals:.2f} minutes per goal"
        return "0.00 minutes per goal"

    
    def total_goals_and_assists(self):
        return f"{self.goals + self.assists} goals and assists total."
    
    def yellow_cards_per_minute(self):
        if self.yellow_cards > 0:
            return f"{self.minutes / self.yellow_cards:.2f} minutes per yellow card"
        return "No yellow cards"

    def xg_per_goal(self):
        if self.goals > 0:
            return f"{self.xg / self.goals:.2f} xG per goal"
        return "0.00 xG per goal"
        
    def contribution_to_team(self):
        if self.match.goals_for > 0:
            return f"{((self.goals + self.assists) / self.match.goals_for) * 100:.2f} % contribution"
        return "0.00 % contribution"


    def __str__(self):
        return f"{self.player.name}, {self.match.home_team} vs. {self.match.away_team}, {self.match.date}"