
from random import randint

class Weapons:
    def __init__(self,):
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
    
    def BreakShield(self, player, enemy):
        enemy.TakeShieldDamage(enemy.shield)
        damage= player.Attack(enemy)
        
        if(damage!=0):
            print(f'You break the shield of the oponent causing {damage} damage\n')
        else:
            print('You breake the shield of the oponent but no cause damage\n')
        
        self.habilitColdown=3

class Spear(Weapons):
    def __init__(self):
        self.weapon="Spear"
        self.damage=3
        self.habilitColdown=1
    
    def Weakness(self, enemy, player):
        enemy.TakeDamage(enemy.TakeShieldDamage(self.damage))
        damage=player.Attack(enemy)
        print(f'The Weakness cause {damage} + {self.damage} damage\n')
        self;habilitColdown=2


class Bow(Weapons):
    def __init__(self):
        self.weapon="Bow"
        self.damage=2
        self.habilitColdown=1
    
    def CriticalHit(self, player, enemy):
        damage=player.Attack(enemy)

        if(damage==0):
            damage=self.damage
        enemy.TakeDamage(damage)
        print(f'You got a Critical Hit causing {2*damage} damage\n')

        self.habilitColdown=3


def randWeapon():
    rand=randint(0,2)
    if(rand==0):
        return Sword()
    elif(rand==1):
        return Spear()
    elif(rand==2):
        return Bow()

