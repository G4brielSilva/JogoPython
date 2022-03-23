from random import randint
from random import choice
from Magics import Magic

# A lot of damage
class Fireball(Magic):
    def __init__(self):
        self.magic = 'Fireball'
        self.magicColdown=2
        self.manaCost=6
    
    def Conjure(self, Wizard, Target):
        damage=randint(1, int(Wizard.manaMax/3))+ randint(1, Wizard.Weapon.power)
        Target.TakeDamage(damage)
        self.magicColdown=3

        if(Wizard.Weapon.weapon=="Orb"):
            self.magicColdown-=1
        
        return damage

# The less fragments, the more damage
class IceFragments(Magic):
    def __init__(self):
        self.magic = 'Ice Fragments'
        self.magicColdown=1
        self.manaCost=8

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
            Target.TakeDamage(eachDamage)
            damage+=eachDamage

        self.magicColdown=2
        return damage


# The lightningBolt Ignore the enemy's Shield
class LightningBolt(Magic):
    def __init__(self):
        self.magic = 'Lightning Bolt'
        self.magicColdown=2
        self.manaCost=5

    def Conjure(self, Wizard, Target):
        chance=choice(["Fail","Hit"])
        damage=0

        self.magicColdown=3

        if chance=="Hit":
            damage=5+Wizard.Weapon.power
            Target.ResetShield()
            Target.TakeDamage(damage)

        return damage
            