from actions import *
from debug import endgame


cont=True

def Continue(player, enemy):
    if((str(input('\ndo you Want to continue?\n[Y] or [N]\n'))[0].upper())=='N'):
        print('\nObrigado por Jogar!\n')
        sleep(1)
        return False
    else:
        print()
        return True


# Loop of the game
while (cont):

    # Creating Player and Enemy
    player, enemy = CreatingCharacters('both')

    # Loop of battle
    while True:
        
        #endgame(player, enemy)

        #MakingPlayerAction(ChoiceAction(player, enemy),player, enemy)
        ShowStatus(player)
        MakingEnemyAction(enemy, player)
        ShowStatus(player)
        ShowStatus(enemy)
        if(FinishHim(player,enemy)):
            break
        sleep(4)
        
        MakingEnemyAction(player, enemy)
        ShowStatus(enemy)

        if(FinishHim(player,enemy)):
            break

        ColdownPassing(player, enemy)

    cont = Continue(player,enemy)
    del enemy,player
    

