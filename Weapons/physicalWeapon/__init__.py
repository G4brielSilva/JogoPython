from random import randint
from random import choice

from Weapons import Weapons


class Sword(Weapons):
    weapon="Sword"
    weaponType="Physical"
    damage=4
    weaponHability = "Break Shield"
    habilityColdown=1

    def __init__(self):
        pass    
    
    # Ignore target's shield and got damage
    def WeaponHability(self, actor, target):
        target.TakeShieldDamage(target.shield)
        damage= actor.Attack(target)
        self.habilityColdown=3
        return damage

class Spear(Weapons):
    weapon="Spear"
    weaponType="Physical"
    damage=3
    habilityColdown=1
    weaponHability = "Weakness"

    def __init__(self):
        pass    
        
    # Got extra 3 damage
    def WeaponHability(self, actor, target):
        target.TakeDamage(target.TakeShieldDamage(3))
        damage=actor.Attack(target)
        self.habilityColdown=2
        return damage


class Bow(Weapons):
    weapon="Bow"
    weaponType="Physical"
    damage=2
    habilityColdown=1
    weaponHability = "Critical Hit"

    def __init__(self):
        pass    
    
    # Causes double damage
    def WeaponHability(self, actor, target):
        damage=actor.Attack(target)

        if(damage==0):
            damage=self.damage
        target.TakeDamage(damage)
        self.habilityColdown=3
        return damage

# choice a randon Weapon
def randPhysicalWeapon():
    return choice([Sword(),Spear(),Bow()])