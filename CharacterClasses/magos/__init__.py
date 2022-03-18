from CharacterClasses.personagem import Personagem
from random import randint


class Mago(Personagem):
    def __init__(self, life=5, attack=2, Weapon=None):
        self.life=life
        self.attack=attack
        self.Weapon=Weapon
        self.shield=0
        self.characterClass="Wizard"
        self.manaMax=randint(7,2*self.life)
        self.mana=manaMax

    # The mage Defensive position has mana which argument
    def Defense(self):
        self.shield+=randint(1,int(self.manaMax/3))

