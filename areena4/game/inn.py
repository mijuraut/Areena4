import random
from .models import Gladiator, Race


def get_dice_sum(amount_of_dies: int) -> int:
    # Throw a 6-sided die amount_of_dies times and return the sum
    dice_sum = sum(random.randint(1, 6) for _ in range(amount_of_dies))
    return dice_sum


class Inn:
    names = [
        "Saffell", "Ateridge", "Cane", "Blackstock", "Fairfax",
        "Edgar", "Rusher", "Wildgoose", "Gooday", "Winder",
        "Wolf", "Whitbread", "Oxer", "Law", "Peppercorn",
        "Sherlock", "Cutbush", "Attwood", "Yatman", "Bird",
        "Greet", "Widdows", "Duke", "Cook", "Saltman",
        "Smith", "Wyman", "Berwick", "Bargate", "Underwood",
        "Bent", "Snowball", "Root", "Benbow", "Aldrich",
        "Raven", "Admer", "Allright", "Yapp", "Baggett",
        "Dale", "Balston", "Powell", "Crane", "Redway",
        "Thatcher", "Westgate", "Nodder", "Tout", "Dearman",
        "Whatman", "Arthur"
    ]
    gladiators = []
    recently_used_names = set()

    @staticmethod
    def create_gladiator():
        if len(Inn.recently_used_names) >= 20:
            Inn.recently_used_names.clear()

        available_names = set(Inn.names) - Inn.recently_used_names
        if not available_names:
            # All names have been recently used, reset the set
            Inn.recently_used_names.clear()

        name = random.choice(list(available_names))
        Inn.recently_used_names.add(name)

        gladiator = Gladiator(name=name)
        Inn.gladiators.append(gladiator)
        return gladiator



inn = Inn()