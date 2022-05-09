from time import sleep
from random import randint
from random import choice

from CharacterClasses.magos import Mago
from CharacterClasses.guerreiro import Guerreiro



# Enemy Choicing an Action
def EnemyChoiceAction(enemy):
    if(enemy.Weapon.weaponType=='Physical'):
        enemysAction = choice(['Attack','Defense','Weapon Hability'])
    elif(enemy.Weapon.weaponType=='Magical'):
        enemysAction=choice(['Attack','Defense','Magics'])
        if(enemysAction=='Magics'):
            enemysAction=choice(['F','I','L'])

    return enemysAction

# Making Enemy Action
def MakingEnemyAction(player, enemy):
    
    # Enemy action
    enemysAction = EnemyChoiceAction(enemy)

    if(enemysAction=='Attack'):
        shield=player.shield
        damage=enemy.Attack(player)
        if(damage!=0):
            if(shield!=0):
                print(f"{-shield}S\n")
            print(f"Enemy cause {damage} of damage\n")
        else:
            print("Enemys Missed Attack!\n")
    elif(enemysAction=='Defense'):
        shield = enemy.Defense()
        print(f"\nEnemy enter in defense position and gain {shield} of shield\n")
    elif(enemysAction=='Weapon Hability'):
        if(enemy.Weapon.habilitColdown!=0):
            shield=player.shield
            damage=enemy.Attack(player)
            if(damage!=0):
                if(shield!=0):
                    print(f"{-shield}S\n")
                print(f"Enemy cause {damage} of damage\n")
            else:
                print("Enemys Missed Attack!\n")
        
        else:
            if(enemy.Weapon.weapon=="Sword"):
                damage=enemy.Weapon.BreakShield(enemy, player)
                if(damage!=0):
                    print(f"The enemy break your shield causing {damage} damage\n")
                else:
                    print("The enemy break your shield but no cause damage\n")
            elif(enemy.Weapon.weapon=="Spear"):
                damage=enemy.Weapon.Weakness(enemy, player)
                print(f"The enemy uses Weakness and cause {damage} + {3} damage\n")
            elif(enemy.Weapon.weapon=="Bow"):
                damage=enemy.Weapon.CriticalHit(enemy, player)
                print(f"The enemy got a Critical Hit causing {2*damage} damage\n")

    elif('FLI'.__contains__(enemysAction)):
    
        if (enemy.magics[enemysAction].magicColdown == 0 and enemy.mana>enemy.magics[enemysAction].manaCost):
            damage=enemy.magics[enemysAction].Conjure(enemy, player)
            mana=enemy.mana>enemy.magics[enemysAction].manaCost

            if enemy.Weapon.weapon=='Orb':
                mana-= enemy.Weapon.bonusManaCost

            enemy.mana-=mana

            if(damage!=0):
                print(f"The enemy conjures {enemy.magics[enemysAction].magic} and causes {damage}\n")
            else:
                print(f"The enemy conjures {enemy.magics[enemysAction].magic} but miss the target\n")
        else:
            MakingEnemyAction(player, enemy)
