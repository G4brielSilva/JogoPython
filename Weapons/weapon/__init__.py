
from random import randint

# Super
class Weapons:
    def __init__(self):
        self.weapon="Weapon"
        self.damage=0
        self.habilitColdown=0
    
    def ColdownPass(self):
        if(self.habilitColdown>0):
            self.habilitColdown-=1

class Sword(Weapons):
    def __init__(self):
        self.weapon="Sword"
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
        self.damage=3
        self.habilitColdown=1
    
    # Got extra 3 damage
    def Weakness(self, enemy, player):
        enemy.TakeDamage(enemy.TakeShieldDamage(self.damage))
        damage=player.Attack(enemy)
        self.habilitColdown=2
        return damage


class Bow(Weapons):
    def __init__(self):
        self.weapon="Bow"
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
def randWeapon():
    rand=randint(0,2)
    if(rand==0):
        return Sword()
    elif(rand==1):
        return Spear()
    elif(rand==2):
        return Bow()

