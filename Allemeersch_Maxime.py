# -*- coding: utf-8 -*-

import random
import datetime


class Player:
    keyboard_key = {'z': (-1, 0),
                    'q': (0, -1),
                    's': (1, 0),
                    'd': (0, 1)}

    def __init__(self, name,start=(0, 0) ,points=0 ):
        self.name = name
        self.points = points
        self.position = start

    def move(self):
        key = input("Mouvement (z,q,s,d) : ")
        while key not in Player.keyboard_key.keys() :
            key = input("Mouvement (z,q,s,d) : ")
        move = Player.keyboard_key[key]
        self.position = (self.position[0] + move[0], self.position[1] + move[1])

class Enemy:
    keyboard_key = {'z': (-1, 0),
                    'q': (0, -1),
                    's': (1, 0),
                    'd': (0, 1)}

    def __init__(self, name,start=(5, 5)):
        self.name = name
        self.position = start

    def move(self):
        key = random.choice('zqsd')
        move = Enemy.keyboard_key[key]
        self.position = (self.position[0] + move[0], self.position[1] + move[1])


class Game:

    def __init__(self, player1, player2, enemy, size=10):
        self.player1 = player1
        self.player2 = player2
        self.enemy = enemy
        self.board_size = size
        self.candies = []
        self.mur = []
        self.candyPartyTrue = 0

    # Dessine le plateau
    def draw(self):
        for line in range(self.board_size):
            for col in range(self.board_size):
                if (line, col) in self.candies:
                    print("*", end=" ")
                elif (line, col) == self.enemy.position:
                    print("X", end=" ")
                elif (line, col) == self.player1.position:
                    print("1", end=" ")
                elif (line, col) == self.player2.position:
                    print("2", end=" ")
                else:
                    print(".", end=" ")
            print()

    # Fait apparaitre un bonbon
    def pop_candy(self):
        new_candy = (random.choice(range(self.board_size)), random.choice(range(self.board_size)))
        if new_candy not in self.candies:
            self.candies.append(new_candy)

    # CandyParty
    def pop_candyParty(self):
        candytSpawn = random.randint(1, 5)
        print("Vous avez trouver un bonbon magique ! ", candytSpawn, " bonbons ont apparut")
        while (candytSpawn != 0):
            new_candy = (random.choice(range(self.board_size)), random.choice(range(self.board_size)))
            if new_candy not in self.candies:
                self.candies.append(new_candy)
            candytSpawn = candytSpawn -1

    def check_Position_TP(self):
        ListA = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ListB = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
        for CheckFirst in ListA :
            for CheckSecond in ListB:
                if self.player1.position == (CheckFirst,CheckSecond): #Vers la gauche Player1
                    self.player1.position = (CheckFirst,9)
                elif self.player1.position == (CheckFirst, 10):  # Vers la droite Player1
                    self.player1.position = (CheckFirst, 0)
                elif self.player1.position == (CheckSecond, CheckFirst): #Vers le Haut Player1
                    self.player1.position = (9, CheckFirst)
                elif self.player1.position == (10, CheckFirst):  # Vers le bas Player1
                    self.player1.position = (0, CheckFirst)

                elif self.player2.position == (CheckFirst, CheckSecond): #Vers la gauche Player2
                    self.player2.position = (CheckFirst, 9)
                elif self.player2.position == (CheckFirst, 10):  # Vers la droite Player2
                    self.player2.position = (CheckFirst, 0)
                elif self.player2.position == (CheckSecond, CheckFirst): #Vers le Haut Player2
                    self.player2.position = (9, CheckFirst)
                elif self.player2.position == (10, CheckFirst): #Vers le bas Player2
                    self.player2.position = (0, CheckFirst)

                elif self.enemy.position == (CheckFirst, CheckSecond): #Vers la gauche Enemy
                    self.enemy.position = (CheckFirst, 9)
                elif self.enemy.position == (CheckFirst, 10):  # Vers la droite Enemy
                    self.enemy.position = (CheckFirst, 0)
                elif self.enemy.position == (CheckSecond, CheckFirst): #Vers le Haut Enemy
                    self.enemy.position = (9, CheckFirst)
                elif self.enemy.position == (10, CheckFirst): #Vers le bas Enemy
                    self.enemy.position = (0, CheckFirst)

    # Regarde s'il y a un bonbon à prendre (et le prend)
    def check_candy(self):
        pointsWin = random.randint(1, 3)
        CandyPartyTrue = random.randint(1, 5)
        if self.player1.position in self.candies:
            print(self.player1.name ,"+",pointsWin, "point(s)")
            self.player1.points += pointsWin
            self.candies.remove(self.player1.position)
            if (CandyPartyTrue >= 4) :
                self.candyPartyTrue = 1

        if self.player2.position in self.candies:
            print(self.player2.name ,"+",pointsWin, "point(s)")
            self.player2.points += pointsWin
            self.candies.remove(self.player2.position)
            if (CandyPartyTrue >= 4) :
                self.candyPartyTrue = 1

        if self.enemy.position in self.candies:
            self.candies.remove(self.enemy.position)


    # Regarde s'il y a un enemy
    def check_Enemy(self):
        if self.player1.position == self.enemy.position:
            print(self.player1.name, " -2 pts")
            self.player1.points -= 2
        elif self.player2.position == self.enemy.position:
            print(self.player2.name, " -2 pts")
            self.player2.points -= 2

    # Joue une partie complète
    def play(self):
        print("--- Début de la partie ---") 
        self.draw()

        end = Game.end_time(1, 0)
        now = datetime.datetime.today()

        while now < end:
            self.enemy.move()
            self.player1.move()
            print(self.player1.position)
            self.check_Position_TP()
            self.player2.move()
            self.check_Position_TP()
            self.check_candy()
            self.check_Enemy()

            if random.randint(1, 3) == 1:
                self.pop_candy()

            if self.candyPartyTrue == 1: #candyParty
                self.candyPartyTrue = 0
                self.pop_candyParty()

            self.draw()

            now = datetime.datetime.today()

        print("----- Terminé -----")
        print(self.player1.name, "vous avez", self.player1.points, "points")
        print(self.player2.name,"vous avez", self.player2.points, "points")

    @staticmethod
    # retourne le moment où le jeu est censé être fini
    def end_time(delta_minute, delta_second):
        delta = datetime.timedelta(minutes=delta_minute, seconds=delta_second)
        end = datetime.datetime.today() + delta
        return end


if __name__ == "__main__":
    p1 = Player("Maxime")
    p2 = Player("Miguel",(0, 9))
    e = Enemy("Lanress")
    g = Game(p1,p2,e)
    g.play()




