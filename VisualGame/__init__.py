from Actions import gameActions
from Sprites.Gdur import GdurSprite
from Sprites import SpritesPath


class Character:
    def __init__(self, char, sprites=None):
        self.Char = char
        self.Spr = sprites

    def set_sprites(self, sprites):
        self.Spr = sprites

#altura
height= 480
#largura
width= 640

x_ground, y_ground = 180, 320


def create_character(flip: bool = False):
    char = Character(gameActions.CreatingCharacters())
    char.set_sprites(GdurSprite())

    char.Spr.defineSprites(SpritesPath.give_path(char.Char),6)
    x_grd = x_ground
    if flip:
        x_grd = x_ground + 80

    char.Spr.setImage(x_grd,y_ground)
    char.Spr.flipSprite(flip)

    return char