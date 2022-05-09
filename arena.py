from Actions import enemysActions
from Actions import playersActions
from Actions import gameActions

from debug import endgame
from time import sleep

cont=True

# Loop of the game
while (cont):

    # Creating Player and Enemy
    player, enemy = gameActions.CreatingCharacters('both')
    #endgame(player, enemy)
    # Loop of battle
    while True:
        
        #playersActionsMakingPlayerAction(playersActions.PlayerChoiceAction(player, enemy),player, enemy)
        gameActions.ShowStatus(player)

        enemysActions.MakingEnemyAction(enemy, player)

        gameActions.ShowStatus(player)
        gameActions.ShowStatus(enemy)
        
        if(gameActions.FinishHim(player,enemy)):
            break
        sleep(4)
        
        enemysActions.MakingEnemyAction(player, enemy)

        gameActions.ShowStatus(enemy)

        if(gameActions.FinishHim(player,enemy)):
            break

        gameActions.ColdownPassing(player, enemy)

    cont = gameActions.Continue(player,enemy)

    del enemy,player
    

