from random import randint
from random import choice
from Magics import Magic

# A lot of damage
class Fireball(Magic):
    magic = 'Fireball'
    magicColdown=2
    manaCost=6

    def __init__(self):
        pass    
        
    def Conjure(self, Wizard, Target):
        damage=randint(1, int(Wizard.manaMax/3))+  randint(1, Wizard.Weapon.power)
        Target.TakeDamage(damage)
        self.magicColdown=3
        
        return damage

# The less fragments, the more damage
class IceFragments(Magic):
    magic = 'Ice Fragments'
    magicColdown=1
    manaCost=8
    
    def __init__(self):
        pass         

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
        chance=choice(["F","H"])
        damage=0

        self.magicColdown=3

        if chance=="H":
            damage=5+Wizard.Weapon.power
            Target.ResetShield()
            Target.TakeDamage(damage)

        return damage

class Magics:

    def __init__(self):
        self.fireball = Fireball()
        self.icefragments = IceFragments()
        self.lightningbolt = LightningBolt()
        self.magics = [self.fireball,self.icefragments,self.lightningbolt]