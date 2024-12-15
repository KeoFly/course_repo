from random import randint
from time import sleep

class Warrior:
    health: int = 100
    attack: int = 20
    endurance: int = 100
    armor: int = 100

warrior1 = Warrior()
warrior2 = Warrior()

def movement(move1, move2, warrior1, warrior2):
    if move1 == 1 and move2 == 1:
        if warrior1.endurance > 0 and warrior2.endurance > 0:
            warrior1.endurance -= 10
            warrior2.endurance -= 10
            warrior2.health -= randint(10, 30)
            warrior1.health -= randint(10, 30)
        elif warrior1.endurance == 0 and warrior2.endurance > 0:
            warrior2.endurance -= 10
            warrior1.health -= randint(10, 30)
            warrior2.health -= randint(0, 10)
        elif warrior1.endurance > 0 and warrior2.endurance == 0:
            warrior1.endurance -= 10
            warrior2.health -= randint(10, 30)
            warrior1.health -= randint(0, 10)
        else:
            warrior1.health -= randint(0, 10)
            warrior2.health -= randint(0, 10)
        print(f"Warriors attack each other."
              f"\n Warrior1 health: {warrior1.health}"
              f"\n Warrior2 health: {warrior2.health}")
        sleep(2)

    elif move1 == 1 and move2 == 2:
        if warrior1.endurance > 0:
            if warrior2.armor > 0:
                warrior1.endurance -= 10
                warrior2.health -= randint(0, 20)
                warrior2.armor -= randint(0, 10)
            else:
                warrior1.endurance -= 10
                warrior2.health -= randint(10, 30)
        else:
            warrior2.health -= randint(0, 10)
        print(f"Warrior1 attacks but warrior2 defends."
              f"\n Warrior1 health: {warrior1.health}"
              f"\n Warrior2 health: {warrior2.health}")
        sleep(2)
    elif move1 == 2 and move2 == 1:
        if warrior2.endurance > 0:
            if warrior1.armor > 0:
                warrior2.endurance -= 10
                warrior1.health -= randint(0, 20)
                warrior1.armor -= randint(0, 10)
            else:
                warrior2.endurance -= 10
                warrior1.health -= randint(10, 30)
        else:
            warrior1.health -= randint(0, 10)
        print(f"Warrior2 attacks but warrior1 defends."
              f"\n Warrior1 health: {warrior1.health}"
              f"\n Warrior2 health: {warrior2.health}")
        sleep(2)
    else:
        print(f"Warriors defend themselves."
              f"\n Warrior1 health: {warrior1.health}"
              f"\n Warrior2 health: {warrior2.health}")
        sleep(2)

while True:
    move1 = randint(1, 2)
    move2 = randint(1, 2)
    movement(move1, move2, warrior1, warrior2)
    if warrior2.health <= 10:
        warrior2.health = 0
        print("Warrior1 won!!!")
        break
    elif warrior1.health <= 10:
        warrior1.health = 0
        print("Warrior2 won!!!")
        break
