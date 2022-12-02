from abc import ABC, abstractclassmethod
# Super
class Weapons(ABC):
    weapon="Weapon"
    weaponType="Weapon"
    damage=0

    @abstractclassmethod
    def __init__(self):    
        self.habilityColdown=0
    
    def ColdownPass(self):
        if(self.habilityColdown>0):
            self.habilityColdown-=1