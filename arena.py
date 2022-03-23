from actions import *

# Creating Player and Enemy
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

print(f"\nYou\nCharacter Class: {player.characterClass}\nWeapon: {player.Weapon.weapon}\nWeapon Damage: {player.Weapon.damage}")
if(playerCharClass=='M'):
    print(f"Mana{player.mana}\nWeapon Power: {player.Weapon.power}\n")
else:
    print()

print(f"Enemy\nCharacter Class: {enemy.characterClass}\nWeapon: {enemy.Weapon.weapon}\nWeapon Damage: {enemy.Weapon.damage}")
if(enemyCharClass=='M'):
    print(f"Weapon Power: {enemy.Weapon.power}")
else:
    print()


# Loop of exec
while True:
    
    MakingPlayerAction(ChoiceAction(player, enemy),player, enemy)

    if(FinishHim(player,enemy)):
            break
    sleep(2)
    
    MakingEnemyAction(player, enemy)

    if(FinishHim(player,enemy)):
        break

    ColdownPassing(player, enemy)