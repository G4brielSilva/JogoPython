from abc import ABC, abstractclassmethod
# Super
class Magic(ABC):
    magic = 'Magic'
    magicColdown = 0
    manaCost = 0

    @abstractclassmethod
    def __init__(self):
        self.magicColdown=3

    def ColdownPass(self, weapon):
        self.magicColdown-=1

        if(weapon=="Grimoire"):
            self.magicColdown-=1
        
        if self.magicColdown < 0:
            self.magicColdown = 0
    
    @abstractclassmethod
    def Conjure(self, Wizard, Target):
        pass