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

    def __init__(self, player1, player2, enemy1,enemy2, size=10):
        self.player1 = player1
        self.player2 = player2
        self.enemy1 = enemy1
        self.enemy2 = enemy2
        self.board_size = size
        self.candies = []
        self.candyPartyTrue = 0
        self.choixLevel = 0
        self.min = 0
        self.sec = 0
        self.WallPassOrNot = 0
        self.candyPartyOrNOT = 0


    # Dessine le plateau
    def draw(self):
        for WalllineTop in range(self.board_size+2):
            print("-", end=" ")
        print()
        for line in range(self.board_size):
            print("|", end=" ") #WalllineRight
            for col in range(self.board_size):
                if (line, col) in self.candies:
                    print("\033[35;1m*\033[0m", end=" ")
                elif (line, col) == self.enemy1.position:
                    print("\033[31;1mX\033[0m", end=" ")
                elif (line, col) == self.enemy2.position:
                    print("\033[31;1mX\033[0m", end=" ")
                elif (line, col) == self.player1.position:
                    print("\033[32;1m1\033[0m", end=" ")
                elif (line, col) == self.player2.position:
                    print("\033[34;1m2\033[0m", end=" ")
                else :
                    print(".", end=" ")

            print("|", end=" ")  # WalllineLeft
            print()
        for WalllineLow in range(self.board_size+2):
            print("-", end=" ")
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

    # Permet au joueur de se téléporter à l'opposé
    def check_Position_TP(self):
        ListA = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ListB = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
        for CheckFirst in ListA :
            for CheckSecond in ListB:
                if self.player1.position == (CheckFirst,CheckSecond): #Vers la gauche Player1
                    self.player1.position = (CheckFirst,self.board_size-1)
                elif self.player1.position == (CheckFirst, self.board_size):  # Vers la droite Player1
                    self.player1.position = (CheckFirst, 0)
                elif self.player1.position == (CheckSecond, CheckFirst): #Vers le Haut Player1
                    self.player1.position = (self.board_size-1, CheckFirst)
                elif self.player1.position == (self.board_size, CheckFirst):  # Vers le bas Player1
                    self.player1.position = (0, CheckFirst)

                elif self.player2.position == (CheckFirst, CheckSecond): #Vers la gauche Player2
                    self.player2.position = (CheckFirst, self.board_size-1)
                elif self.player2.position == (CheckFirst, self.board_size):  # Vers la droite Player2
                    self.player2.position = (CheckFirst, 0)
                elif self.player2.position == (CheckSecond, CheckFirst): #Vers le Haut Player2
                    self.player2.position = (self.board_size-1, CheckFirst)
                elif self.player2.position == (self.board_size, CheckFirst): #Vers le bas Player2
                    self.player2.position = (0, CheckFirst)

                elif self.enemy1.position == (CheckFirst, CheckSecond): #Vers la gauche Enemy
                    self.enemy1.position = (CheckFirst, self.board_size-1)
                elif self.enemy1.position == (CheckFirst, self.board_size):  # Vers la droite Enemy
                    self.enemy1.position = (CheckFirst, 0)
                elif self.enemy1.position == (CheckSecond, CheckFirst): #Vers le Haut Enemy
                    self.enemy1.position = (self.board_size-1, CheckFirst)
                elif self.enemy1.position == (self.board_size, CheckFirst): #Vers le bas Enemy
                    self.enemy1.position = (0, CheckFirst)

                elif self.enemy2.position == (CheckFirst, CheckSecond): #Vers la gauche Enemy
                    self.enemy2.position = (CheckFirst, self.board_size-1)
                elif self.enemy2.position == (CheckFirst, self.board_size):  # Vers la droite Enemy
                    self.enemy2.position = (CheckFirst, 0)
                elif self.enemy2.position == (CheckSecond, CheckFirst): #Vers le Haut Enemy
                    self.enemy2.position = (self.board_size-1, CheckFirst)
                elif self.enemy2.position == (self.board_size, CheckFirst): #Vers le bas Enemy
                    self.enemy2.position = (0, CheckFirst)

    #Permet de bloquer le passage des murs
    def check_Wall(self):
        ListA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ListB = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        for CheckFirst in ListA:
            for CheckSecond in ListB:
                if self.player1.position == (CheckFirst, CheckSecond):  # Vers la gauche Player1
                    self.player1.position = (CheckFirst, CheckSecond+1)
                elif self.player1.position == (CheckFirst, self.board_size):  # Vers la droite Player1
                    self.player1.position = (CheckFirst, self.board_size-1)
                elif self.player1.position == (CheckSecond, CheckFirst):  # Vers le Haut Player1
                    self.player1.position = (CheckSecond+1, CheckFirst)
                elif self.player1.position == (self.board_size, CheckFirst):  # Vers le bas Player1
                    self.player1.position = (self.board_size-1, CheckFirst)

                elif self.player2.position == (CheckFirst, CheckSecond):  # Vers la gauche Player2
                    self.player2.position = (CheckFirst, CheckSecond+1)
                elif self.player2.position == (CheckFirst, self.board_size):  # Vers la droite Player2
                    self.player2.position = (CheckFirst, self.board_size-1)
                elif self.player2.position == (CheckSecond, CheckFirst):  # Vers le Haut Player2
                    self.player2.position = (CheckSecond+1, CheckFirst)
                elif self.player2.position == (self.board_size, CheckFirst):  # Vers le bas Player2
                    self.player2.position = (self.board_size-1, CheckFirst)

                elif self.enemy1.position == (CheckFirst, CheckSecond):  # Vers la gauche Enemy
                    self.enemy1.position = (CheckFirst, CheckSecond+1)
                elif self.enemy1.position == (CheckFirst, self.board_size):  # Vers la droite Enemy
                    self.enemy1.position = (CheckFirst, self.board_size-1)
                elif self.enemy1.position == (CheckSecond, CheckFirst):  # Vers le Haut Enemy
                    self.enemy1.position = (CheckSecond+1, CheckFirst)
                elif self.enemy1.position == (self.board_size, CheckFirst):  # Vers le bas Enemy
                    self.enemy1.position = (self.board_size-1, CheckFirst)

                elif self.enemy2.position == (CheckFirst, CheckSecond):  # Vers la gauche Enemy
                    self.enemy2.position = (CheckFirst, CheckSecond+1)
                elif self.enemy2.position == (CheckFirst, self.board_size):  # Vers la droite Enemy
                    self.enemy2.position = (CheckFirst, self.board_size-1)
                elif self.enemy2.position == (CheckSecond, CheckFirst):  # Vers le Haut Enemy
                    self.enemy2.position = (CheckSecond+1, CheckFirst)
                elif self.enemy2.position == (self.board_size, CheckFirst):  # Vers le bas Enemy
                    self.enemy2.position = (self.board_size-1, CheckFirst)

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

        if self.enemy1.position in self.candies:
            self.candies.remove(self.enemy1.position)
        if self.enemy2.position in self.candies:
            self.candies.remove(self.enemy2.position)


        # Regarde s'il y a un enemy

    def check_Enemy(self):
        if self.player1.position == self.enemy1.position or self.player1.position == self.enemy2.position :
            if self.player1.points <= 10:
                print(self.player1.name, " -2 pts")
                self.player1.points -= 2
            elif self.player1.points > 10:
                 print(self.player1.name, " -",self.player1.points," pts")
                 self.player1.points -= self.player1.points
        elif self.player2.position == self.enemy1.position or self.player2.position == self.enemy2.position:
            if self.player2.points <= 10:
                print(self.player2.name, " -2 pts")
                self.player2.points -= 2
            elif self.player2.points > 10:
                print(self.player2.name, " -",self.player2.points," pts")
                self.player2.points -= self.player2.points

    #Enregistre le score
    def StoreLeaderBoard(self):
        fi = open('Leaderboard.txt','a')
        fi.write(str(self.player1.points)) #Enregistre le score Player1
        fi.write(' ')
        fi.write(self.player1.name) #Enregistre le nom Player1
        fi.write('\n')
        fi.write(str(self.player2.points)) #Enregistre le score Player2
        fi.write(' ')
        fi.write(self.player2.name) #Enregistre le nom Player2
        fi.write('\n')
        print('score enregistrer')
        fi.close

    def displayLeaderboard(self):
        print("--- Score ---")
        fi = open('Leaderboard.txt','r')
        lines = fi.readlines()
        fi.close
        for line in lines:
            print(line.strip())
        self.menu()

    #LastPosition
    def LastPosition(self):
        self.player1.lastPosition = self.player1.position
        self.player2.lastPosition = self.player2.position

        # Joue une partie complète

    def menu(self):
        print("--- Menu ---")
        print("Niveau Normal (1): 1min, 2 ennemi, mur bloquer et bonus")
        print("Personnaliser (2) ")
        print("Tableau des scores  (3) ")
        self.choixLevel = int(input("Niveau : "))
        if self.choixLevel == 1 :
            self.play()
        elif self.choixLevel == 2:
            self.min = int(input("Combien de minute ?  : "))
            self.sec = int(input("Combien de seconde ?  : "))
            self.WallPassOrNot = int(
                input("Permettre de passer à travers les murs et de réapparaitre de l’autre côté ? Oui (1) / Non (2) : "))
            self.candyPartyOrNOT = int(input("Permettre de mettre des bonus en jeu ? Oui (1) / Non (2) : "))
            self.play()
        elif self.choixLevel == 3 :
            self.displayLeaderboard()

    def play(self):
        if self.choixLevel == 1 :
            print("--- Début de la partie Normal ---")

            self.draw()

            end = Game.end_time(1, 0)
            now = datetime.datetime.today()

            while now < end:
                self.enemy1.move()
                self.enemy2.move()
                self.player1.move()
                self.check_Wall()
                self.player2.move()
                self.check_Wall()
                self.check_candy()
                self.check_Enemy()

                if random.randint(1, 3) == 1:
                    self.pop_candy()

                if self.candyPartyTrue == 1:  # candyParty
                    self.candyPartyTrue = 0
                    self.pop_candyParty()

                self.draw()

                now = datetime.datetime.today()

        elif self.choixLevel == 2 : #Try Catch
            print("--- Début de la partie Personalisé ---")

            self.draw()

            end = Game.end_time(self.min, self.sec)
            now = datetime.datetime.today()

            while now < end:
                self.enemy1.move()
                self.enemy2.move()
                self.player1.move()
                self.player2.move()
                if self.WallPassOrNot == 1 :
                    self.check_Position_TP()
                elif self.WallPassOrNot == 2:
                    self.check_Wall()
                self.check_Enemy()
                self.check_candy()


                if random.randint(1, 3) == 1:
                    self.pop_candy()

                if self.candyPartyOrNOT == 1 :
                    if self.candyPartyTrue == 1: #candyParty
                        self.candyPartyTrue = 0
                        self.pop_candyParty()

                self.draw()

                now = datetime.datetime.today()

        print("----- Terminé -----")
        print(self.player1.name, "vous avez", self.player1.points, "points")
        print(self.player2.name,"vous avez", self.player2.points, "points")
        self.StoreLeaderBoard()
        self.menu()

    @staticmethod
    # retourne le moment où le jeu est censé être fini
    def end_time(delta_minute, delta_second):
        delta = datetime.timedelta(minutes=delta_minute, seconds=delta_second)
        end = datetime.datetime.today() + delta
        return end

if __name__ == "__main__":
    NamePlayer1 = input("Nom du joueur 1 : ")
    NamePlayer2 = input("Nom du joueur 2 : ")
    p1 = Player(NamePlayer1)
    p2 = Player(NamePlayer2,(0, 9))
    e1 = Enemy("Enemy1",(7,2))
    e2 = Enemy("Enemy2",(7,7))
    g = Game(p1,p2,e1,e2)
    g.menu()




