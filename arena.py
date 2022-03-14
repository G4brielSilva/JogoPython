from time import sleep
from personagem import Personagem
from random import randint
from weapon import *




player= Personagem (randint(5,15),randint(1,3),randWeapon())
enemy= Personagem (randint(5,15),randint(1,3),randWeapon())

print(f'You: Weapon:{player.Weapon.weapon} Damage:{player.Weapon.damage}')
print(f'Enemy: Weapon:{enemy.Weapon.weapon} Damage:{enemy.Weapon.damage}\n')

weapon=player.Weapon.weapon

def FinishHim(play, enem)-> bool:
    if(enem.life<=0):
        print('Parabéns você venceu!')
        return True
    elif(play.life<=0):
        print('Poxa, você perdeu!')
        return True
    else:
        return False
    

while True:
    print(f'You: L:{player.life}\tEnemy: L:{enemy.life} S:{enemy.shield}')
    
    print("Choice a Action:")
    print("[A] Attack\n[D] Defense")
    if(weapon=="Sword"):
        print(f"[B] BreakShield CD:{player.Weapon.habilitColdown}\n")
    elif(weapon=="Spear"):
        print(f"[W] Weakness CD:{player.Weapon.habilitColdown}\n")
    elif(weapon=="Bow"):
        print(f"[C] CriticalHit CD:{player.Weapon.habilitColdown}\n")
    choice=input().lower()

    if(choice=="a"):
        damage=player.Attack(enemy)
        if(damage!=0):
            print(f'You cause {damage} of damage')
        if(FinishHim(player,enemy)):
            break
        if(damage!=0):
            print(f'Enemy take {damage} of damage L:{enemy.life}\n')
        else:
            print("Missed Attack!\n")

    elif(choice=="d"):
        player.Defense()
        print(f'\nYou enter in defense position and gain {player.shield} of shield')
        print(f'You: L:{player.life} S:{player.shield}\n')
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
            if(damage!=0):
                print(f'You cant use the Weapon Habilit, but you Attack and cause {damage} of damage')
            
    if(FinishHim(player,enemy)):
            break
    sleep(2)
    if(randint(0,1)==0):
        damage=enemy.Attack(player)
        if(damage!=0):
            print(f'Enemy cause {damage} of damage')
        else:
            print("Missed Attack!\n")
    else:
        enemy.Defense()
        print(f"\nEnemy enter in defense position and gain {enemy.shield} of shield")

    if(FinishHim(player,enemy)):
        break
    player.Weapon.ColdownPass()
    enemy.Weapon.ColdownPass()