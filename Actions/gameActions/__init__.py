from time import sleep
from random import randint, choice

from CharacterClasses.classes import Mago, Guerreiro

# Passing Coldown
def ColdownPassing(actor,target):
    # Passing coldown os habilitys
    #Refatorar
    if(actor.Weapon.weaponType=='Physical'):
        actor.Weapon.ColdownPass()
    else:
        for magic in actor.magics.magics:
            magic.ColdownPass(actor.Weapon.weapon)
    
    if(target.Weapon.weaponType=='Physical'):
        target.Weapon.ColdownPass()
    else:
        for magic in target.magics.magics:
            magic.ColdownPass(target.Weapon.weapon)


# Creating actor and target
# two is type of return
def CreatingCharacters(two = False):
    def ChoiceClass():
        match(choice(['M','W'])):
            case 'M':
                return Mago()
            case 'W':
                return Guerreiro()
    
    if two:
            return ChoiceClass(), ChoiceClass()
    return ChoiceClass()


# Show Status
def ShowStatus(char, showHability = False):
    print(f"""
Life: {char.life}    
Shield: {char.shield}
Weapon: {char.Weapon.weapon}
    """)
    try:
        print(f'Mana: {char.mana}')
    except:
        pass

    if showHability:
        match(char.charClass):
            case 'Wizard':
                magics = char.magics
                final_str = f'{magics.magicColdown}\tMana Cost: {magics.manaCost}'

                print(f"""

[M] Meditate

[F] Fireball CD: {final_str}
[I] Ice Fragments CD: {final_str}
[L] LightningBolt CD: {final_str}\n     
        """)
            case 'Warior':
                weapon= char.Weapon
                print(f""""

[{weapon.weaponHability[0]}] {weapon.weaponHability} - {weapon.habilityColdown}\n
        """)


# checking if the fight is over
def FinishHim(actor, target):
    if(target.life<=0):
        print("Parabéns você venceu!")
        return True
    elif(actor.life<=0):
        print("Poxa, você perdeu!")
        return True
    else:
        return False

# If the actor wants to continue
def Continue():
    if((str(input('\ndo you Want to continue?\n[Y] or [N]\n'))[0].upper())=='N'):
        print('\nObrigado por Jogar!\n')
        sleep(1)
        return False
    else:
        print()
        return True