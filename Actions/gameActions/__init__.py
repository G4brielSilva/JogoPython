from time import sleep
from random import randint
from random import choice

from CharacterClasses.magos import Mago
from CharacterClasses.guerreiro import Guerreiro


# Passing Coldown
def ColdownPassing(player,enemy):
    # Passing coldown os habilitys
    if(player.Weapon.weaponType=='Physical'):
        player.Weapon.ColdownPass()
    else:
        for magic in player.magics.values():
            magic.ColdownPass()
    
    if(enemy.Weapon.weaponType=='Physical'):
        enemy.Weapon.ColdownPass()
    else:
        for magic in enemy.magics.values():
            magic.ColdownPass()


# Creating Player and Enemy
def CreatingCharacters(ret):
    playerCharClass= str(input('Select a Character Class:\n[M]-Mage\n[W]-Warior\n'))[0].upper()

    if playerCharClass=='M':
        player= Mago()
    elif playerCharClass=='W':
        player = Guerreiro()

    enemyCharClass = choice(['M','W'])

    if enemyCharClass=='M':
        enemy= Mago()
    elif enemyCharClass=='W':
        enemy = Guerreiro()

    if ret =='both':
        return player,enemy
    elif ret == 'enemy':
        return enemy
    elif ret =='player':
        return player


# Show Status
def ShowStatus(Character):
    print(f"""
Life: {Character.life}    
Shield: {Character.shield}
Weapon: {Character.Weapon.weapon}
    """)
    if(Character.Weapon.weaponType=='Magical'):
        print(f"""
Mana: {Character.mana}

[F] CD:{Character.magics['F'].magicColdown}
[I] CD:{Character.magics['I'].magicColdown}
[L] CD:{Character.magics['L'].magicColdown}\n      
        """)

# checking if the fight is over
# play == player
# enem == enemy
def FinishHim(player, enemy):
    if(enemy.life<=0):
        print("Parabéns você venceu!")
        return True
    elif(player.life<=0):
        print("Poxa, você perdeu!")
        return True
    else:
        return False

# If the player wants to continue
def Continue(player, enemy):
    if((str(input('\ndo you Want to continue?\n[Y] or [N]\n'))[0].upper())=='N'):
        print('\nObrigado por Jogar!\n')
        sleep(1)
        return False
    else:
        print()
        return True