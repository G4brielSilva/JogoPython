from random import randint
from random import choice

from Weapons import Weapons


class Staff(Weapons):
    weapon = "Staff"
    weaponType = "Magical"
    damage = 1
    __magicPowerBonus = randint(1,2)
    power= 4 + __magicPowerBonus
    passive={'Passive': "Magic Penetration",'Description': f"The staff have a Bonus of Magic Power {power-__magicPowerBonus} + {__magicPowerBonus}"}

    def __init__(self):
        pass
class Orb(Weapons):
    weapon="Orb"
    weaponType="Magical"
    damage=0
    bonusManaCost = randint(1, 3)
    power=3

    passive={'Passive': "Spiritual Blessing",'Description': f"Reduce the mana cost in {bonusManaCost}"}

    def __init__(self):
        pass

class Grimoire(Weapons):

    weapon="Grimoire"
    weaponType="Magical"
    damage=1
    power=2

    passive={'Passive': "Arcane Wisdom",'Description': f"Reduce the magic coldown in 1 turn"}

    def __init__(self):
        pass    

# choice a randon Weapon
def randMagicalWeapon():
    return choice([Staff(),Orb(),Grimoire()])