from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=16)
    gold = models.IntegerField(default=1500)
    division = models.IntegerField(default=4)
    points = models.IntegerField(default=0)
    is_in_cup = models.BooleanField(default=True)
    last_season_placement = models.PositiveIntegerField(null=True)
    championship_wins = models.IntegerField(default=0)
    cup_wins = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=50, unique=True)
    size = models.IntegerField(default=6)
    image = models.ImageField(upload_to='static/', null=True, blank=True)
    amount_of_dies_hit_points = models.IntegerField()
    amount_of_dies_strength = models.IntegerField()
    amount_of_dies_speed = models.IntegerField()
    amount_of_dies_mana = models.IntegerField()
    added_value_hit_points = models.IntegerField()
    added_value_strength = models.IntegerField()
    added_value_speed = models.IntegerField()
    added_value_mana = models.IntegerField()

    def __str__(self):
        return self.name

    @classmethod
    def get_random_race(cls):
        # Get all races
        all_races = cls.objects.all()

        if all_races:
            # Return a random race
            return random.choice(all_races)
        else:
            # No races available
            return None

class Gladiator(models.Model):
    name = models.CharField(max_length=16)
    salary = models.IntegerField(null=True)
    wounded_months = models.IntegerField(default=0)
    age = models.IntegerField(null=True)
    knockouts_season = models.IntegerField(default=0)
    knockouts_total = models.IntegerField(default=0)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    has_movement_left = models.BooleanField(default=True)
    max_hit_points = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    melee_damage_bonus = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    spell_skill = models.IntegerField(default=0)
    mana = models.IntegerField(default=0)
    spear_hit = models.IntegerField(default=0)
    sword_hit = models.IntegerField(default=0)
    axe_hit = models.IntegerField(default=0)
    club_hit = models.IntegerField(default=0)
    spear_parry = models.IntegerField(default=0)
    sword_parry = models.IntegerField(default=0)
    axe_parry = models.IntegerField(default=0)
    club_parry = models.IntegerField(default=0)
    fist_hit = models.IntegerField(default=0)
    bow_hit = models.IntegerField(default=0)
    crossbow_hit = models.IntegerField(default=0)
    evade = models.IntegerField(default=0)
    resist_spell = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    def __str__(self):
        return (f" {self.race.name} {self.name}, {self.team.name} ")


# class Month(models.Model):
#     name = models.CharField(max_length=20)  # e.g., January, February, etc.
#     race_of_the_month = models.ForeignKey(Race, on_delete=models.CASCADE)
#
# class Schedule(models.Model):
#     team = models.OneToOneField('Team', on_delete=models.CASCADE)
#
