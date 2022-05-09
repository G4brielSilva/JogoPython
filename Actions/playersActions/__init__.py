
# Choicing The Player Action
def PlayerChoiceAction(player,enemy):
    print(f"You: L:{player.life}")
    if(player.Weapon.weaponType=='Magical'):
        print(f"M: {player.mana}\n")

    print(f"Enemy: L:{enemy.life} S:{enemy.shield}")
    if(enemy.Weapon.weaponType=='Magical'):
        print(f"M: {enemy.mana}")


    print("\nChoice a Action:")
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
        print(f"[M] Meditate")
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
            if(choice=="M"):
                ManaGain=player.Meditate()
                if(ManaGain!=0):
                    print(f"\nYou Meditate and recovered {ManaGain} points of mana")
                else:
                    print(f"\nYou Meditate, but you already have maximum of mana!")

            elif(player.magics[choice].magicColdown==0):
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
                    MakingPlayerAction(PlayerChoiceAction(player, enemy), player, enemy)
            else:
                print(f"Spell in Coldown, select other action\n")
                MakingPlayerAction(PlayerChoiceAction(player, enemy), player, enemy)