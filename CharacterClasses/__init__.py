# >>>PERSONAGEM<<<<
# >Stats<
# Life
# Attack
# Weapon
# Shield
# Mana

# >Actions<
# Attack
# Defense
# Hability Weapon

# >Magic<
# Fireball
# IceFragments
# LightningBolt
from random import randint


class Personagem:
    shield=0
    characterClass="class"
    life=0
    attack=0
    Weapon="weapon"
    shield=0
    
    #Creating a Character
    def __init__(self):
        pass
        
        
    # Atacking the enemy
    def Attack(self, target):
        self.ResetShield()
        damage= target.TakeShieldDamage(randint(0,self.attack)+randint(0,self.Weapon.damage))

        target.TakeDamage(damage)
        return damage
    
    # Enter in defensive position
    def Defense(self):
        self.ResetShield()
        self.shield+=randint(1,self.attack)

    # Take Damage
    def TakeDamage(self, damage):
        self.life-=damage
        if(self.life<=0):
            self.life==0

    # Take Damage on shield
    def TakeShieldDamage(self, damage):
        dmg=damage-self.shield
        if(dmg>=0):
            self.shield=0
            return dmg
        else:
            self.shield= -dmg
            return 0
    
    # Turn the Shield to 0
    def ResetShield(self):
        self.shield=0
        