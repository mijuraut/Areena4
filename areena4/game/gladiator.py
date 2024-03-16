import random
from .models import Race


def get_toughness(self) -> int:
    """
    Calculate the toughness of the Gladiator.

    The toughness is calculated based on various attributes of the Gladiator,
    such as hit points, strength, speed, mana, weapon hits, and parries.

    Returns:
        int: The calculated toughness value.
    """
    toughness = 0
    toughness += (self.hit_points - 8) * 1.5  # OK
    toughness += self.strength
    toughness += self.speed
    toughness += self.mana
    toughness += self.spear_hit - 10
    toughness += self.spear_parry - 10
    toughness += self.sword_hit - 10
    toughness += self.sword_parry - 10
    toughness += self.axe_hit - 10
    toughness += self.axe_parry - 10
    toughness += self.club_hit - 10
    toughness += self.club_parry - 10

    return toughness


def calculate_salary(self) -> int:
    """
    Calculate the salary of the Gladiator based on age.

    The salary is determined using a base salary and age factors specified
    in the age_factors dictionary. The calculated salary is then rounded to
    the nearest integer.
    """
    base_salary = self.calculate_toughness() / 5
    # salary += (self.hit_points - 7)
    # salary += (self.strength)

    age_factors = {
        20: 1.0,
        21: 0.824,
        22: 0.696,
        23: 0.588,
        24: 0.510,
        25: 0.441,
        26: 0.392,
        27: 0.343,
        28: 0.304,
        29: 0.275,
        30: 0.245,
        31: 0.225,
        32: 0.206,
        33: 0.186,
        34: 0.167,
        35: 0.157
    }

    # Get the age factor, default to 1.0 if the age is not in the dictionary
    age_factor = age_factors.get(self.age, 1.0)

    # Calculate the salary based on the base salary and age factor
    calculated_salary = base_salary * age_factor

    # Round the result to an integer
    rounded_salary = round(calculated_salary)

    return rounded_salary


def get_dice_sum(count):
    return sum(random.randint(1, 6) for _ in range(count))


def assign_attributes(self):
    race = self.race
    weapon_base = self.speed + 10

    self.max_hit_points = get_dice_sum(race.amount_of_dies_hit_points) + race.added_value_hit_points
    self.strength = get_dice_sum(race.amount_of_dies_strength) + race.added_value_strength
    self.speed = get_dice_sum(race.amount_of_dies_speed) + race.added_value_speed
    self.mana = get_dice_sum(race.amount_of_dies_mana) + race.added_value_mana
    self.hit_points = self.max_hit_points
    self.spear_hit = weapon_base + int(random.randint(0, 10))
    self.spear_parry = weapon_base + int(random.randint(0, 10))
    self.sword_hit = weapon_base + int(random.randint(0, 10))
    self.sword_parry = weapon_base + int(random.randint(0, 10))
    self.axe_hit = weapon_base + int(random.randint(0, 10))
    self.axe_parry = weapon_base + int(random.randint(0, 10))
    self.club_hit = weapon_base + int(random.randint(0, 10))
    self.club_parry = weapon_base + int(random.randint(0, 10))
    self.evade = weapon_base + int(random.randint(0, 10))
    self.mana = self.spell_skill
    self.resist_spell = self.spell_skill + int(random.randint(0, 10))