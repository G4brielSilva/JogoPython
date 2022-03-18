from random import randint
from random import choice

from CharacterClasses.magos import Mago


#super
class Magic:
    def __init__(self):
        self.magicColdown=3

    def ColdownPass(self):
        if(self.magicColdown>0):
            self.magicColdown-=1
    
    def Conjure(self, Wizard, Target):
        pass

# A lot of damage
class Fireball(Magic):
    def __init__(self):
        self.magicColdown=2
    
    def Conjure(self, Wizard, Target):
        damage=randint(1, int(Wizard.manaMax/3))+ randint(1, Wizard.Weapon.power)
        target.TakeDamage(damage)
        self.magicColdown=3
        return damage

# The less fragments, the more damage
class IceFragments(Magic):
    def __init__(self):
        selg.magicColdown=1

    def Conjure(self, Wizard, Target):
        fragments=choice([2,4,6])

        bonus=0

        if(fragments==2):
            bonus=2
        elif(fragments==4):
            bonus=1

        eachDamage=choice([1,2]) + bonus
        damage=0

        for frag in range(1,fragments):
            damage+=Target.TakeDamage(eachDamage)

        self.magicColdown=2
        return damage


# The lightningBolt Ignore the enemy's Shield
class LightningBolt(Magic):
    def __init__(self):
        selg.magicColdown=2

    def Conjure(self, Wizard, Target):
        chance=["fail","Fail","Hit"]
        damage=0

        self.magicColdown=3

        if chance=="Hit":
            damage=5
            Target.ResetShield()
            Target.TakeDamage(damage)

        return damage
            