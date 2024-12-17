from random import randint
from time import sleep

class Warrior:
    def __init__(self, name):
        self.name = name

    health: int = 100
    attack: int = 20
    endurance: int = 100
    armor: int = 100


class Battle:
    def __init__(self, first_warrior, second_warrior):
        self.first_warrior = first_warrior
        self.second_warrior = second_warrior

    def move(self, move1, move2, first_warrior, second_warrior):
        if move1 == 1 and move2 == 1:
            if first_warrior.endurance > 0 and second_warrior.endurance > 0:
                first_warrior.endurance -= 10
                second_warrior.endurance -= 10
                second_warrior.health -= randint(10, 30)
                first_warrior.health -= randint(10, 30)
            elif first_warrior.endurance == 0 and second_warrior.endurance > 0:
                second_warrior.endurance -= 10
                first_warrior.health -= randint(10, 30)
                second_warrior.health -= randint(0, 10)
            elif first_warrior.endurance > 0 and second_warrior.endurance == 0:
                first_warrior.endurance -= 10
                second_warrior.health -= randint(10, 30)
                first_warrior.health -= randint(0, 10)
            else:
                first_warrior.health -= randint(0, 10)
                second_warrior.health -= randint(0, 10)
            print(f"Warriors attack each other."
                  f"\n {first_warrior.name} health: {first_warrior.health}"
                  f"\n {second_warrior.name} health: {second_warrior.health}")
            sleep(1)
        elif move1 == 1 and move2 == 2:
            if first_warrior.endurance > 0:
                if second_warrior.armor > 0:
                    first_warrior.endurance -= 10
                    second_warrior.health -= randint(0, 20)
                    second_warrior.armor -= randint(0, 10)
                else:
                    first_warrior.endurance -= 10
                    second_warrior.health -= randint(10, 30)
            else:
                second_warrior.health -= randint(0, 10)
            print(f"{first_warrior.name} attacks but {second_warrior.name} defends."
                  f"\n {first_warrior.name} health: {first_warrior.health}"
                  f"\n {second_warrior.name} health: {second_warrior.health}")
            sleep(1)
        elif move1 == 2 and move2 == 1:
            if second_warrior.endurance > 0:
                if first_warrior.armor > 0:
                    second_warrior.endurance -= 10
                    first_warrior.health -= randint(0, 20)
                    first_warrior.armor -= randint(0, 10)
                else:
                    second_warrior.endurance -= 10
                    first_warrior.health -= randint(10, 30)
            else:
                first_warrior.health -= randint(0, 10)
            print(f"{second_warrior.name} attacks but {first_warrior.name} defends."
                  f"\n {first_warrior.name} health: {first_warrior.health}"
                  f"\n {second_warrior.name} health: {second_warrior.health}")
            sleep(1)
        else:
            print(f"Warriors defend themselves."
                  f"\n {first_warrior.name} health: {first_warrior.health}"
                  f"\n {second_warrior.name} health: {second_warrior.health}")
            sleep(1)

    def fight(self):
        while True:
            move1 = randint(1, 2)
            move2 = randint(1, 2)
            self.move(move1, move2, self.first_warrior, self.second_warrior)
            if self.second_warrior.health <= 10:
                self.second_warrior.health = 0
                winner = f"{self.first_warrior.name}"
                break
            elif self.first_warrior.health <= 10:
                self.first_warrior.health = 0
                winner = f"{self.second_warrior.name}"
                break
        return print(f"{winner} won!!!\n")



warrior1 = Warrior("Ray")
warrior2 = Warrior("John")
warrior3 = Warrior("Boba")
warrior4 = Warrior("Rex")
battle1 = Battle(warrior1, warrior2)
battle2 = Battle(warrior3, warrior4)
battle1.fight()
battle2.fight()
