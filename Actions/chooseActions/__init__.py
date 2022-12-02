from random import choice

from Actions.gameActions import ShowStatus
from Actions.characterActions import Attack,Defense,Hability,Magic,Meditate


# Making Action
def MakingAction(actor, target, action: str):
    match(action):
        case 'A':
            print('Opa')
            return Attack(actor, target)
        case 'D':
            return Defense(actor)
        case 'W':
            return Hability(actor, target)
        case 'M':
            return Meditate(actor)
        case _:
            magics = 'IFL'
            if(action in magics):
                return Magic(actor, target,action)

# Choicing The actor's Action
def ChoiceAction(actor,target, action: str = '@' , human = True):
    if human:
        ShowStatus(actor)
        # print("\nChoice a Action:\n")
        # action = input()[0].upper()
    else:
        classe = actor.characterClass
        # A - Attack
        # D - Defense
        choices = ['A','D']

        if(classe == 'Warior'):
            # W - Weapon Hability
            action = choice(choices.append('W'))
        elif(classe == 'Wizard'):
            # M - Meditate
            # F - Fireball
            # L - Lightning Bolt
            # I - Ice Fragments
            action=choice(choices+['M','F','I','L'])

    return MakingAction(actor, target, action)