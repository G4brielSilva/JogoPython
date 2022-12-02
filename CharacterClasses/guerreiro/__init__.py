from random import randint

from Weapons.physicalWeapon import randPhysicalWeapon
from CharacterClasses import Personagem

class Guerreiro(Personagem):
    characterClass="Warior"
    shield=0

    def __init__(self):
        self.life=randint(16, 32)
        self.attack=randint(2, 6)
        self.Weapon=randPhysicalWeapon()