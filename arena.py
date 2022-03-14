from time import sleep
from personagem import Personagem
from random import randint
from weapon import *


# Creating Player and Enemy
player= Personagem (randint(5,15),randint(1,3),randWeapon())
enemy= Personagem (randint(5,15),randint(1,3),randWeapon())

print(f'You: Weapon:{player.Weapon.weapon} Damage:{player.Weapon.damage}')
print(f'Enemy: Weapon:{enemy.Weapon.weapon} Damage:{enemy.Weapon.damage}\n')

# saving gun for later
weapon=player.Weapon.weapon

# checking if the fight is over
# play == player
# enem == enemy
def FinishHim(play, enem)-> bool:
    if(enem.life<=0):
        print('Parabéns você venceu!')
        return True
    elif(play.life<=0):
        print('Poxa, você perdeu!')
        return True
    else:
        return False
    
# Loop of exec
while True:
    print(f'You: L:{player.life}\tEnemy: L:{enemy.life} S:{enemy.shield}')


    print("Choice a Action:")
    print("[A] Attack\n[D] Defense")

    # Weapons Habilitys
    if(weapon=="Sword"):
        print(f"[B] BreakShield CD:{player.Weapon.habilitColdown}\n")
    elif(weapon=="Spear"):
        print(f"[W] Weakness CD:{player.Weapon.habilitColdown}\n")
    elif(weapon=="Bow"):
        print(f"[C] CriticalHit CD:{player.Weapon.habilitColdown}\n")
    choice=input().lower()

    # Attacking
    if(choice=="a"):
        shield=enemy.shield #guardando escudo perdido
        damage=player.Attack(enemy) #realizando ataque
        if(damage!=0):
            if(shield!=0):
                print(f'{-shield}S\n')
            print(f'You cause {damage} of damage')
            if(FinishHim(player,enemy)):
                break
            print(f'Enemy LifeL:{enemy.life}\n')
        else:
            print("Missed Attack!\n")
    # Defensing
    elif(choice=="d"):
        player.Defense()
        print(f'\nYou enter in defense position and gain {player.shield} of shield')
        print(f'You: L:{player.life} S:{player.shield}\n')
    # Got Hability
    else:
        if(player.Weapon.habilitColdown==0):
            if (weapon=="Sword" and choice=="b"):
                player.Weapon.BreakShield(player,enemy)
            elif(weapon=="Spear" and choice=="w"):
                player.Weapon.Weakness(enemy,player)
            elif(weapon=="Bow" and choice=="c"):
                player.Weapon.CriticalHit(player,enemy)
        else:
            damage=player.Attack(enemy)
            print('You cant use the Weapon Habilit, but you Attack')
            if(damage!=0):
                print(f' and cause {damage} of damage')
            else:
                print("and missed Attack!\n")
        
    if(FinishHim(player,enemy)):
            break
    sleep(2)
    
    # Enemy action
    enemysAction=randint(0,2)

    if(enemysAction==0):
        shield=player.shield
        damage=enemy.Attack(player)
        if(damage!=0):
            if(shield!=0):
                print(f'{-shield}S\n')
            print(f'Enemy cause {damage} of damage\n')
        else:
            print("Enemys Missed Attack!\n")
    elif(enemysAction==1):
        enemy.Defense()
        print(f"\nEnemy enter in defense position and gain {enemy.shield} of shield")
    elif(enemysAction==2):
        if(enemy.Weapon.habilitColdown!=0):
            shield=player.shield
            damage=enemy.Attack(player)
            if(damage!=0):
                if(shield!=0):
                    print(f'{-shield}S\n')
                print(f'Enemy cause {damage} of damage\n')
            else:
                print("Enemys Missed Attack!\n")
        
        else:
            if(enemy.Weapon.weapon=="Sword"):
                damage=enemy.Weapon.BreakShield(enemy, player)
                if(damage!=0):
                    print(f'The enemy break your shield causing {damage} damage\n')
                else:
                    print('The enemy break your shield but no cause damage\n')
            elif(enemy.Weapon.weapon=="Spear"):
                damage=enemy.Weapon.Weakness(enemy, player)
                print(f'The enemy uses Weakness and cause {damage-3} + {3} damage\n')
            elif(enemy.Weapon.weapon=="Bow"):
                damage=enemy.Weapon.CriticalHit(player, enemy)
                print(f'The enemy got a Critical Hit causing {2*damage} damage\n')

    if(FinishHim(player,enemy)):
        break

    # Passing coldown os habilitys
    player.Weapon.ColdownPass()
    enemy.Weapon.ColdownPass()