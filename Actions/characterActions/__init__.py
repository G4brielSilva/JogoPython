def Attack(actor, target):
        shield=target.shield
        damage=actor.Attack(target)

        if(damage!=0):
            if(shield!=0):
                print(f"{-shield}S\n")
            print(f"Causes {damage} of damage\n")
        else:
            print("Missed Attack!\n")
    

def Defense(actor):
    shield = actor.Defense(actor)
    print(f"\nEnter in defense position and gain {shield} of shield\n")


def Hability(actor, target):
    weapon = actor.Weapon.weapon

    if(actor.Weapon.habilitColdown!=0):
        print("Can't use the Weapon Habilit, but Attack")
        Attack(actor, target)
    else:
        match(weapon):
            case 'Sword':
                damage=actor.Weapon.BreakShield(actor, target)
                if(damage!=0):
                    print(f"The shield was breaking causing {damage} damage\n")
                else:
                    print("The shield was breaking but no cause damage\n")
            case 'Spear':
                damage=actor.Weapon.Weakness(actor, target)
                print(f"Uses Weakness and cause {damage} + {3} damage\n")
            case 'Bow':
                damage=actor.Weapon.CriticalHit(actor, target)
                print(f"Got a Critical Hit causing {2*damage} damage\n")

def Magic(actor, target, action = ''):
    def SelectMagic():
        magic = actor.magics
        print(magic.fireball != None)
        match(action):
            case 'F':
                return magic.fireball
            case 'I':
                return magic.icefragments
            case 'L':
                return magic.lightningbolt

    magic = SelectMagic()
    print(magic.magic)

    if (magic.magicColdown == 0 and actor.mana > magic.manaCost):
        damage = magic.Conjure(actor, target)

        actor.PayMana(magic.manaCost)

        if(damage>=0):
            print(f"Conjures {magic.magic} and causes {damage}\n")
        else:
            print(f"Conjures {magic.magic} but miss the target\n")
    else:
        print(f"Don't have mana to Conjure this Spell, maybe is better stop and meditate\n")
        Meditate(actor=actor)


def Meditate(actor):
    ManaGain=actor.Meditate()
    if(ManaGain!=0):
        print(f"\nRelax, Meditate and recovered {ManaGain} points of mana")
    else:
        print(f"\nRelax, Meditate, butalready have maximum of mana!")
