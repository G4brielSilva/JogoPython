from random import randint
from random import choice

from Weapons import Weapons


class Sword(Weapons):
    def __init__(self):
        self.weapon="Sword"
        self.weaponType="Physical"
        self.damage=4
        self.habilitColdown=1
    
    # Ignore enemy's shield and got damage
    def BreakShield(self, player, enemy):
        enemy.TakeShieldDamage(enemy.shield)
        damage= player.Attack(enemy)
        self.habilitColdown=3
        return damage

class Spear(Weapons):
    def __init__(self):
        self.weapon="Spear"
        self.weaponType="Physical"
        self.damage=3
        self.habilitColdown=1
    
    # Got extra 3 damage
    def Weakness(self, player, enemy):
        enemy.TakeDamage(enemy.TakeShieldDamage(3))
        damage=player.Attack(enemy)
        self.habilitColdown=2
        return damage


class Bow(Weapons):
    def __init__(self):
        self.weapon="Bow"
        self.weaponType="Physical"
        self.damage=2
        self.habilitColdown=1
    
    # Causes double damage
    def CriticalHit(self, player, enemy):
        damage=player.Attack(enemy)

        if(damage==0):
            damage=self.damage
        enemy.TakeDamage(damage)
        self.habilitColdown=3
        return damage

# choice a randon Weapon
def randPhysicalWeapon():
    return choice([Sword(),Spear(),Bow()])