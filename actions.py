from time import sleep
from random import randint
from random import choice

from CharacterClasses.magos import Mago
from CharacterClasses.guerreiro import Guerreiro


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

# Choicing The Player Action
def ChoiceAction(player,enemy):
    print(f"You: L:{player.life}")
    if(player.Weapon.weaponType=='Magical'):
        print(f"M: {player.mana}\n")

    print(f"Enemy: L:{enemy.life} S:{enemy.shield}")
    if(enemy.Weapon.weaponType=='Magical'):
        print(f"M: {enemy.mana}\n")


    print("Choice a Action:")
    print("[A] Attack\n[D] Defense")

    if(player.Weapon.weaponType=='Physical'):
        # Weapons Habilitys
        if(player.Weapon.weapon=="Sword"):
            print(f"[B] BreakShield CD:{player.Weapon.habilitColdown}\n")
        elif(player.Weapon.weapon=="Spear"):
            print(f"[W] Weakness CD:{player.Weapon.habilitColdown}\n")
        elif(player.Weapon.weapon=="Bow"):
            print(f"[C] CriticalHit CD:{player.Weapon.habilitColdown}\n")
        choice=input()[0].upper()
    elif(player.Weapon.weaponType=='Magical'):
        # Magics
        print(f"""
[F] Fireball CD:{player.magics['F'].magicColdown}\tMana Cost: {player.magics['F'].manaCost}
[I] Ice Fragments CD:{player.magics['I'].magicColdown}\tMana Cost: {player.magics['I'].manaCost}
[L] LightningBolt CD:{player.magics['L'].magicColdown}\tMana Cost: {player.magics['L'].manaCost}\n
""")
        choice=input()[0].upper()
    return choice

# Making Player Action
def MakingPlayerAction(choice, player, enemy):
    # Attacking
    if(choice=="A"):
        shield=enemy.shield #guardando escudo perdido
        damage=player.Attack(enemy) #realizando ataque
        if(damage!=0):
            if(shield!=0):
                print(f"{-shield}S\n")
            print(f"You cause {damage} of damage")
            if(enemy.life<0):
                enemy.life=0
            print(f"Enemy Life L:{enemy.life}\n")
        else:
            print("Missed Attack!\n")
    # Defensing
    elif(choice=="D"):
        player.Defense()
        print(f"\nYou enter in defense position and gain {player.shield} of shield")
        print(f"You: L:{player.life} S:{player.shield}")

        if(player.Weapon.weaponType=='Magical'):
            print(f"M: {player.mana}\n")
    # Got Hability
    else:
        if player.Weapon.weaponType=='Physical':
            if(player.Weapon.habilitColdown==0):
                if (player.Weapon.weapon=="Sword" and choice=="B"):
                    shield=player.shield
                    damage = player.Weapon.BreakShield(player,enemy)
                    if(damage!=0):
                        if(shield!=0):
                            print(f"\n{-shield}S\n")
                        print(f"You break the enemy's shield causing {damage} damage\n")
                    else:
                        print("You enemy break the enemy's shield but no cause damage\n")
                elif(player.Weapon.weapon=="Spear" and choice=="W"):
                    damage=player.Weapon.Weakness(player,enemy)
                    print(f"You uses Weakness and cause {damage-3} + {3} damage\n")
                elif(player.Weapon.weapon=="Bow" and choice=="C"):
                    damage=player.Weapon.CriticalHit(player,enemy)
                    print(f"You got a Critical Hit causing {2*damage} damage\n")
            else:
                damage=player.Attack(enemy)
                print("You can't use the Weapon Habilit, but you Attack")
                if(damage!=0):
                    print(f" and cause {damage} of damage")
                else:
                    print("and missed Attack!\n")
        
        elif player.Weapon.weaponType=='Magical':
            if(player.magics[choice].magicColdown==0):
                if(player.mana>= player.magics[choice].manaCost):
                    damage=player.magics[choice].Conjure(player, enemy)
                    manaCost=player.magics[choice].manaCost

                    if(player.Weapon.weapon=='Orb'):
                        manaCost-=player.Weapon.bonusManaCost
                    player.mana-=manaCost
                    
                    if(damage!=0):
                        print(f"You conjures the {player.magics[choice].magic} and causes {damage} damage\n")
                    else:
                        print(f"You conjures the {player.magics[choice].magic} but you miss the target\n")
                else:
                    print(f"You don't have mana to Conjure this Spell, select other action\n")
                    MakingPlayerAction(ChoiceAction(player, enemy), player, enemy)
            else:
                print(f"Spell in Coldown, select other action\n")
                MakingPlayerAction(ChoiceAction(player, enemy), player, enemy)
                
# Making Enemy Action
def MakingEnemyAction(player, enemy):
    
    # Enemy action
    if enemy.Weapon.weaponType=='Physical':
        enemysAction=choice(['Attack','Defense','Weapon Hability'])

    elif enemy.Weapon.weaponType=='Magical':
        magics=['F','I','L']
        enemysAction=choice(['Attack','Defense',magics])

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
        enemy.Defense()
        print(f"\nEnemy enter in defense position and gain {enemy.shield} of shield\n")
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

    elif(enemysAction==magics):
        enemysAction=choice(magics)

        ct=0
        while (enemy.magics[enemysAction].magicColdown == 0 or enemy.mana>enemy.magics[enemysAction].manaCost) and ct<9:
            enemysAction=choice(magics.filter(enemysAction, magics))
            ct+=1
        if ct<9:
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


# Passing Coldown
def ColdownPassing(Player,Enemy):
    # Passing coldown os habilitys
    if(Player.Weapon.weaponType=='Physical'):
        Player.Weapon.ColdownPass()
    else:
        for magic in Player.magics.values():
            magic.ColdownPass()
    
    if(Enemy.Weapon.weaponType=='Physical'):
        Enemy.Weapon.ColdownPass()
    else:
        for magic in Enemy.magics:
            print(magic)
            magic.ColdownPass()