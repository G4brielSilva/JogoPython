from CharacterClasses import Personagem
from PIL import Image
import pygame


class Sprite(pygame.sprite.Sprite):

    def __init__(self,spriteWidth = 0,spriteHeight = 0,spriteScale = 0):
        pygame.sprite.Sprite.__init__(self)
        
        self.path = "./Recursos/Images/AnimationSprites/CharacterSprites/"
        self.__sprites = []
        self.__actual = 0
        self.__fliped = False
        self.__animated = False
        
        
        self.__define_whs__(spriteWidth = spriteWidth, spriteHeight=spriteHeight,spriteScale=spriteScale)

    def __define_whs__(self,spriteWidth: int,spriteHeight: int,spriteScale: int):
        self.__spritesWidth = spriteWidth
        self.__spritesHeight = spriteHeight
        self.__spriteScale = spriteScale
    
    def defineSprites(self, path, scale):
        self.path += f"{path}/{path}"

        for i in range(1,4):
            spritePath = f"{self.path}{str(i)}.png"

            if(i==1):
                w,h = get_width_heigth(spritePath)
                self.__define_whs__(w,h,scale)
            self.__sprites.append(pygame.image.load(spritePath))

    
    def __transformImage__(self):
        self.image = pygame.transform.scale(self.image, (self.__spritesWidth*self.__spriteScale, self.__spritesHeight*self.__spriteScale))

    
    def setImage(self,x,y):
        self.__actual = 0
        self.image = self.__sprites[self.__actual]

        self.__transformImage__()

        self.rect = self.image.get_rect()
        self.rect.topleft = x,y

    
    def animate(self):
        self.__animated = True

    
    def update(self):
        if(self.__animated):
            self.__actual += 0.15

            if(self.__actual>=len(self.__sprites)):
                self.__actual=0
                self.__animated = False

            self.image = self.__sprites[int(self.__actual)]
            self.__transformImage__()

            if((self.__fliped)):
                self.flipSprite()

    
    def flipSprite(self,flip=False):
        if(flip):
            self.__fliped=flip

        if(self.__fliped):
            self.image = pygame.transform.flip(self.image, True, False)

        return self.__fliped
    



class SpritesPath():
    sword = "GdurSA"
    spear = "GdurEA"
    bow = "GdurAA"
    staff = "GdurCA"
    orb = "GdurOA"
    grimoire = "GdurGA"

    def give_path(char: Personagem):
        match(char.Weapon.weapon):
            case "Sword": return SpritesPath.sword
            case "Spear": return SpritesPath.spear
            case "Bow": return SpritesPath.bow

            case "Orb": return SpritesPath.orb
            case "Staff": return SpritesPath.staff
            case "Grimoire": return SpritesPath.grimoire

    
def get_width_heigth(filepath: str):
    img = Image.open(filepath)

    width = img.width
    height = img.height

    del(img)

    return width, height