# Super
class Weapons:
    def __init__(self):
        self.weapon="Weapon"
        self.weaponType="Weapon"
        self.damage=0
        self.habilitColdown=0
    
    def ColdownPass(self):
        if(self.habilitColdown>0):
            self.habilitColdown-=1