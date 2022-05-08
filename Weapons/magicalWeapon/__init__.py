from random import randint
from random import choice

from Weapons import Weapons


class Staff(Weapons):

    def __init__(self):
        self.weapon="Staff"
        self.weaponType="Magical"
        self.damage=1

        self.__magicPowerBonus=randint(1,2)
        self.power=4+self.__magicPowerBonus

        self.passive={'Passive': "Magic Penetration",'Description': f"The staff have a Bonus of Magic Power {self.power-self.__magicPowerBonus} + {self.__magicPowerBonus}"}

class Orb(Weapons):
    def __init__(self):
        self.weapon="Orb"
        self.weaponType="Magical"
        self.damage=0
        self.bonusManaCost = randint(1, 3)
        self.power=3

        self.passive={'Passive': "Spiritual Blessing",'Description': f"Reduce the mana cost in {self.bonusManaCost}"}

class Grimoire(Weapons):
    def __init__(self):
        self.weapon="Grimoire"
        self.weaponType="Magical"
        self.damage=1
        self.power=2

        self.passive={'Passive': "Arcane Wisdom",'Description': f"Reduce the magic coldown in 1 turn"}

# choice a randon Weapon
def randMagicalWeapon():
    return choice([Staff(),Orb(),Grimoire()])