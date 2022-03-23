#super
class Magic:
    def __init__(self):
        self.magicColdown=3

    def ColdownPass(self):
        if(self.magicColdown>0):
            self.magicColdown-=1
    
    def Conjure(self, Wizard, Target):
        pass