from random import randint

from CharacterClasses import Personagem
from Magics.magic import Magics
from Weapons.magicalWeapon import randMagicalWeapon

class Mago(Personagem):
    
    

    def __init__(self):
        self.life= randint(12,24)
        self.attack= randint(1, 3)
        self.Weapon=randMagicalWeapon()
        self.characterClass="Wizard"
        self.manaMax=randint(7,2*self.life)
        self.mana=self.manaMax
        self.magics = Magics()

    # The mage Defensive position has Max of mana which argument
    def Defense(self):
        shield = randint(1,int(self.manaMax/3))
        self.shield= shield
        return shield
    
    # The mage take a turn to medidate and gain mana points
    def Meditate(self):
        mana=randint(1,int(self.manaMax/2))
        self.mana+=mana

        if(self.mana>self.manaMax):
            self.mana=self.manaMax
            return self.manaMax-self.mana
        
        return mana
    
    def PayMana(self, mana):
        weapon =  self.Weapon.weapon
        if weapon == 'Orb':
            mana -= weapon.bonusManaCost
        
        self.mana -= mana