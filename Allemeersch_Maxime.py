# -*- coding: utf-8 -*-
# -*- Create By Allemeersch Maxime -*-

import random
import datetime
import codecs #Permet de d'afficher un fichier en UTF-8
import webbrowser


class Player:
    keyboard_key = {'z': (-1, 0),
                    'q': (0, -1),
                    's': (1, 0),
                    'd': (0, 1)}

    def __init__(self, name,start=(0, 0) ,points=0 ):
        self._name = name
        self._points = points
        self._position = start
        self._last_position = start


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def points(self):
        return self._points
    @points.setter
    def points(self, new_points):
        self._points = new_points

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, position):
        self._position = position

    @property
    def lastPosition(self):
        return self._last_position
    @lastPosition.setter
    def lastPosition(self, last_position):
        self._last_position = last_position

    @property
    def newPosition(self):
        return self._new_position
    @newPosition.setter
    def newPosition(self, new_position):
        self._new_position = new_position

    def move(self):
        key = input("Mouvement (z,q,s,d) : ")
        while key not in Player.keyboard_key.keys():
            key = input(" Erreur : Mouvement (z,q,s,d) : ")
        move = Player.keyboard_key[key]
        self._new_position = (self._position[0] + move[0], self._position[1] + move[1])

        if  self._last_position != self._new_position:
            self._last_position = self._position
            self._position = self._new_position

class Enemy:
    keyboard_key = {'z': (-1, 0),
                    'q': (0, -1),
                    's': (1, 0),
                    'd': (0, 1)}

    def __init__(self,start=(5, 5)):
        self._position = start

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, new_position):
        self._position = new_position

    def move(self):
        key = random.choice('zqsd')
        move = Enemy.keyboard_key[key]
        self._position = (self._position[0] + move[0], self._position[1] + move[1])

class Game:

    def __init__(self, player1, player2, enemy1,enemy2, size=10):
        self._player1 = player1
        self._player2 = player2
        self._enemy1 = enemy1
        self._enemy2 = enemy2
        self._board_size = size
        self._candies = []
        self._candyPartyTrue = 0
        self._candyPartyNumberCandy = 0
        self._choiceLevel = 0
        self._min = 0
        self._sec = 0
        self._wallPassOrNot = 0
        self._candyPartyOrNOT = 0
        self._candyOutOfDateOrNot = 0

    @property
    def player1(self):
        return self._player1
    @player1.setter
    def player1(self, new_player1):
        self._player1 = new_player1

    @property
    def player2(self):
        return self._player2
    @player2.setter
    def player2(self, new_player2):
        self._player2 = new_player2

    @property
    def enemy1(self):
        return self._enemy1
    @enemy1.setter
    def enemy1(self, new_enemy1):
        self._enemy1 = new_enemy1

    @property
    def enemy2(self):
        return self._enemy2
    @enemy2.setter
    def enemy2(self, new_enemy2):
        self._enemy2 = new_enemy2

    @property
    def size(self):
        return self._board_size
    @size.setter
    def size(self, new_board_size):
        self._board_size = new_board_size

    @property
    def candies(self):
        return self._candies
    @candies.setter
    def candies(self, new_candies):
        self._candies = new_candies

    @property
    def candyPartyTrue(self):
        return self._candyPartyTrue
    @candyPartyTrue.setter
    def candyPartyTrue(self, new_candyPartyTrue):
        self._candyPartyTrue = new_candyPartyTrue

    @property
    def candyPartyNumberCandy(self):
        return self._candyPartyNumberCandy
    @candyPartyNumberCandy.setter
    def candyPartyNumberCandy(self, new_candyPartyNumberCandy):
        self._candyPartyNumberCandy = new_candyPartyNumberCandy

    @property
    def choiceLevel(self):
        return self._choiceLevel
    @choiceLevel.setter
    def choiceLevel(self, new_choiceLevel):
        self._choiceLevel = new_choiceLevel

    @property
    def min(self):
        return self._min
    @min.setter
    def min(self, new_min):
        self._min = new_min

    @property
    def sec(self):
        return self._sec
    @sec.setter
    def sec(self, new_sec):
        self._sec = new_sec

    @property
    def wallPassOrNot(self):
        return self._wallPassOrNot
    @wallPassOrNot.setter
    def wallPassOrNot(self, new_wallPassOrNot):
        self._wallPassOrNot = new_wallPassOrNot

    @property
    def candyPartyOrNOT(self):
        return self._candyPartyOrNOT
    @candyPartyOrNOT.setter
    def candyPartyOrNOT(self, new_candyPartyOrNOT):
        self._candyPartyOrNOT = new_candyPartyOrNOT

    @property
    def candyOutOfDateOrNot(self):
        return self._candyOutOfDateOrNot
    @candyOutOfDateOrNot.setter
    def candyOutOfDateOrNot(self, new_candyOutOfDateOrNot):
        self._candyOutOfDateOrNot = new_candyOutOfDateOrNot

    #Dessine le plateau
    def draw(self):
        for wallLineTop in range(self._board_size):
            print("◼", end=" ") #wallLineTop
            #print("\033[36;1m◼\033[0m", end=" ") #wallLineTop Color
        print()

        for line in range(self._board_size):
            print("◼", end=" ") #wallLineRight
            #print("\033[36;1m◼\033[0m", end=" ") #wallLineRight Color
            for col in range(self._board_size):
                if (line, col) in self._candies:
                    print("*", end=" ")
                    #print("\033[35;1mO\033[0m", end=" ")  #Ici j'ai voulu mettre des couleurs, cependant les couleurs ne fonctionne pas avec IDLE python.
                elif (line, col) == self.player1._position:
                    print("1", end=" ")
                    #print("\033[32;1m1\033[0m", end=" ")
                elif (line, col) == self.player2._position:
                    print("2", end=" ")
                    #print("\033[34;1m2\033[0m", end=" ")
                elif (line, col) == self.enemy1._position:
                    print("X", end=" ")
                    #print("\033[31;1mX\033[0m", end=" ")
                elif (line, col) == self.enemy2._position:
                    print("X", end=" ")
                    #print("\033[31;1mX\033[0m", end=" ")
                else :
                    print(".", end=" ")

            print("◼", end=" ")  #wallLineLeft
            #print("\033[36;1m◼\033[0m", end=" ")  # wallLineLeft Color
            print()
        for wallLineLow in range(self._board_size):
            print("◼", end=" ") #wallLineLow
            #print("\033[36;1m◼\033[0m", end=" ") #wallLineLow Color
        print()

    #Fait apparaitre un bonbon
    def pop_candy(self):
        new_candy = (random.choice(range(self._board_size)), random.choice(range(self._board_size)))
        if new_candy not in self._candies and new_candy not in self.player1._position  and new_candy not in self.enemy1._position and new_candy not in self.enemy2._position:
            self._candies.append(new_candy)

    #CandyParty
    def pop_candyParty(self):
        candytSpawn = random.randint(1, 5)
        print("Vous avez trouvé un bonbon magique ! ", candytSpawn, " bonbons ont apparut")
        while (candytSpawn != 0):
            new_candy = (random.choice(range(self._board_size)), random.choice(range(self._board_size)))
            if new_candy not in self._candies and new_candy not in self.player1._position and new_candy not in self.enemy1._position and new_candy not in self.enemy2._position:
                self._candies.append(new_candy)
            candytSpawn = candytSpawn -1

    #Regarde s'il y a un bonbon à prendre (et le prend)
    def check_candy(self):
        pointsWin = random.randint(1, 3)
        if self.player1._position in self._candies:
            print(self.player1._name ,"+",pointsWin, "point(s)")
            self.player1._points += pointsWin
            self._candies.remove(self.player1._position)
            self.candyPartyNumberCandy = random.randint(1, 5)

        if self.player2._position in self._candies:
            print(self.player2._name ,"+",pointsWin, "point(s)")
            self.player2._points += pointsWin
            self._candies.remove(self.player2._position)
            self.candyPartyNumberCandy = random.randint(1, 5)

        if self.enemy1._position in self._candies :
            self._candies.remove(self.enemy1._position)

        if self.enemy2._position in self._candies:
            self._candies.remove(self.enemy2._position)

        if self.candyPartyNumberCandy >= 5:
            self.candyPartyNumberCandy = 0 #Je remet à 0 pour éviter que les ennemis prend un bonbon et remet des bonbons bonus
            self._candyPartyTrue = 1

    #Regarde s'il y a un bonbon périmé à prendre (et le prend)
    def check_candy_out_of_date(self):
        if self.player1._position in self._candies:
            print("Non ! ",self.player1._name , " a perdu - 5 points , car il a mangé un bonbon périmé")
            self.player1._points -= 5
            self._candies.remove(self.player1._position)

        if self.player2._position in self._candies:
            print("Non ! ",self.player2._name , " a perdu - 5 points , car il a mangé un bonbon périmé")
            self.player2._points -= 5
            self._candies.remove(self.player2._position)

        if self.enemy1._position in self._candies:
            self._candies.remove(self.enemy1._position)

        if self.enemy2._position in self._candies:
            self._candies.remove(self.enemy2._position)

    #Permet au joueur de ce téléporter à l'opposer
    def check_Position_TP(self):
        ListA = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ListB = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
        for CheckFirst in ListA :
            for CheckSecond in ListB:
                if self.player1._position == (CheckFirst,CheckSecond): #Vers la gauche Player1
                    self.player1._position = (CheckFirst,self._board_size-1)
                elif self.player1._position == (CheckFirst, self._board_size):  # Vers la droite Player1
                    self.player1._position = (CheckFirst, 0)
                elif self.player1._position == (CheckSecond, CheckFirst): #Vers le Haut Player1
                    self.player1._position = (self._board_size-1, CheckFirst)
                elif self.player1._position == (self._board_size, CheckFirst):  # Vers le bas Player1
                    self.player1._position = (0, CheckFirst)

                elif self.player2._position == (CheckFirst, CheckSecond): #Vers la gauche Player2
                    self.player2._position = (CheckFirst, self._board_size-1)
                elif self.player2._position == (CheckFirst, self._board_size):  # Vers la droite Player2
                    self.player2._position = (CheckFirst, 0)
                elif self.player2._position == (CheckSecond, CheckFirst): #Vers le Haut Player2
                    self.player2._position = (self._board_size-1, CheckFirst)
                elif self.player2._position == (self._board_size, CheckFirst): #Vers le bas Player2
                    self.player2._position = (0, CheckFirst)

                elif self.enemy1._position == (CheckFirst, CheckSecond): #Vers la gauche Enemy
                    self.enemy1._position = (CheckFirst, self._board_size-1)
                elif self.enemy1._position == (CheckFirst, self._board_size):  # Vers la droite Enemy
                    self.enemy1._position = (CheckFirst, 0)
                elif self.enemy1._position == (CheckSecond, CheckFirst): #Vers le Haut Enemy
                    self.enemy1._position = (self._board_size-1, CheckFirst)
                elif self.enemy1._position == (self._board_size, CheckFirst): #Vers le bas Enemy
                    self.enemy1._position = (0, CheckFirst)

                elif self.enemy2._position == (CheckFirst, CheckSecond): #Vers la gauche Enemy
                    self.enemy2._position = (CheckFirst, self._board_size-1)
                elif self.enemy2._position == (CheckFirst, self._board_size):  # Vers la droite Enemy
                    self.enemy2._position = (CheckFirst, 0)
                elif self.enemy2._position == (CheckSecond, CheckFirst): #Vers le Haut Enemy
                    self.enemy2._position = (self._board_size-1, CheckFirst)
                elif self.enemy2._position == (self._board_size, CheckFirst): #Vers le bas Enemy
                    self.enemy2._position = (0, CheckFirst)

    #Permet de bloquer le passage des murs
    def check_Wall(self):
        ListA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ListB = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        for CheckFirst in ListA:
            for CheckSecond in ListB:
                if self.player1._position == (CheckFirst, CheckSecond):  # Vers la gauche Player1
                    self.player1._position = (CheckFirst, CheckSecond+1)
                elif self.player1._position == (CheckFirst, self._board_size):  # Vers la droite Player1
                    self.player1._position = (CheckFirst, self._board_size-1)
                elif self.player1._position == (CheckSecond, CheckFirst):  # Vers le Haut Player1
                    self.player1._position = (CheckSecond+1, CheckFirst)
                elif self.player1._position == (self._board_size, CheckFirst):  # Vers le bas Player1
                    self.player1._position = (self._board_size-1, CheckFirst)

                elif self.player2._position == (CheckFirst, CheckSecond):  # Vers la gauche Player2
                    self.player2._position = (CheckFirst, CheckSecond+1)
                elif self.player2._position == (CheckFirst, self._board_size):  # Vers la droite Player2
                    self.player2._position = (CheckFirst, self._board_size-1)
                elif self.player2._position == (CheckSecond, CheckFirst):  # Vers le Haut Player2
                    self.player2._position = (CheckSecond+1, CheckFirst)
                elif self.player2._position == (self._board_size, CheckFirst):  # Vers le bas Player2
                    self.player2._position = (self._board_size-1, CheckFirst)

                elif self.enemy1._position == (CheckFirst, CheckSecond):  # Vers la gauche Enemy
                    self.enemy1._position = (CheckFirst, CheckSecond+1)
                elif self.enemy1._position == (CheckFirst, self._board_size):  # Vers la droite Enemy
                    self.enemy1._position = (CheckFirst, self._board_size-1)
                elif self.enemy1._position == (CheckSecond, CheckFirst):  # Vers le Haut Enemy
                    self.enemy1._position = (CheckSecond+1, CheckFirst)
                elif self.enemy1._position == (self._board_size, CheckFirst):  # Vers le bas Enemy
                    self.enemy1._position = (self._board_size-1, CheckFirst)

                elif self.enemy2._position == (CheckFirst, CheckSecond):  # Vers la gauche Enemy
                    self.enemy2._position = (CheckFirst, CheckSecond+1)
                elif self.enemy2._position == (CheckFirst, self._board_size):  # Vers la droite Enemy
                    self.enemy2._position = (CheckFirst, self._board_size-1)
                elif self.enemy2._position == (CheckSecond, CheckFirst):  # Vers le Haut Enemy
                    self.enemy2._position = (CheckSecond+1, CheckFirst)
                elif self.enemy2._position == (self._board_size, CheckFirst):  # Vers le bas Enemy
                    self.enemy2._position = (self._board_size-1, CheckFirst)

    #Regarde s'il y a un ennemi
    def check_Enemy(self):
        if self.player1._position == self.enemy1._position or self.player1._position == self.enemy2._position :
            if self.player1._points <= 10:
                print(self.player1._name, " -2 pts")
                self.player1._points -= 2
            elif self.player1._points > 10:
                 print(self.player1._name, " -",self.player1._points," pts")
                 self.player1._points -= 0
        elif self.player2._position == self.enemy1._position or self.player2._position == self.enemy2._position:
            if self.player2._points <= 10:
                print(self.player2._name, " -2 pts")
                self.player2._points -= 2
            elif self.player2._points > 10:
                print(self.player2._name, " -",self.player2._points," pts")
                self.player2._points -= 0
    #Enregistre le score
    def storeLeaderBoard(self):
        with open('Leaderboard.txt','a') as fi:
            fi.write(str(self.player1._points)) #Enregistre le score Player1
            fi.write(' ')
            fi.write(self.player1._name) #Enregistre le nom Player1
            fi.write('\n')
            fi.write(str(self.player2._points)) #Enregistre le score Player2
            fi.write(' ')
            fi.write(self.player2._name) #Enregistre le nom Player2
            fi.write('\n')

    #Affiche le score
    def displayLeaderboard(self):
        print("--- Score ---")
        with  open('Leaderboard.txt','r') as fi:
            lines = fi.readlines()
            for line in lines:
                print(line.strip())
            self.menu()

    def displayReadme(self):
        print("--- Readme ---")
        s = codecs.open('README.md', 'r', 'utf-8')
        print ('fichier lu = ', s.read())
        self.menu()

    #Menu
    def menu(self):
        print("--- Menu ---")
        print("Niveau Normal (1): 1min, 2 ennemis, mur bloquer et bonus")
        print("Difficle (2) : 1min, 2 ennemis avec 3 mouvements, moins de spawn de bonbon, bonbon périmé")
        print("Personnalisé (3) : Paramétrer la partie ")
        print("Tableau des scores (4) ")
        print("Afficher le Readme (5) ")
        print("GitHub du projet (6) ")
        try:
            self._choiceLevel = int(input("Choix : "))
            ListMenu = [1, 2, 3, 4, 5, 6]
            while self._choiceLevel not in ListMenu :
                self._choiceLevel = int(input("Numéro invalide! Choix : "))
            if self._choiceLevel == 1:
                self.play()
            elif self._choiceLevel == 2:
                self.play()
            elif self._choiceLevel == 3:
                self._min = int(input("Combien de minute ?  : "))
                self._sec = int(input("Combien de seconde ?  : "))
                while self._wallPassOrNot != 1 and self._wallPassOrNot != 2 :
                    self._wallPassOrNot = int(input("Permettre de passer à travers les murs et de réapparaitre de l’autre côté ? Oui (1) / Non (2) : "))
                while self._candyPartyOrNOT != 1 and self._candyPartyOrNOT != 2:
                    self._candyPartyOrNOT = int(input("Mettre des bonus en jeu ? Oui (1) / Non (2) : "))
                while self._candyOutOfDateOrNot != 1 and self._candyOutOfDateOrNot != 2:
                    self._candyOutOfDateOrNot = int(input("Mettre des malus en jeu ? Oui (1) / Non (2) : "))
                self.play()
            elif self._choiceLevel == 4 :
                self.displayLeaderboard()
            elif self._choiceLevel == 5 :
                self.displayReadme()
            elif self._choiceLevel == 6 :
                webbrowser.open("https://github.com/LeigerMax/ExamenPython")
                self.menu()
        except ValueError:
            print("Valeur incorrect ! \n")
            self.menu()

    # Joue une partie complète
    def play(self):
        if self._choiceLevel == 1:
            print("--- Début de la partie Normal ---")

            self.draw()

            end = Game.end_time(1, 0)
            now = datetime.datetime.today()

            while now < end:
                self.player1.move()
                self.player2.move()
                self.check_candy()
                self.enemy1.move()
                self.enemy2.move()
                self.check_Wall()
                self.check_candy()
                self.check_Enemy()

                if random.randint(1, 3) == 1:
                    self.pop_candy()

                if self._candyPartyTrue == 1:  # candyParty
                    self._candyPartyTrue = 0
                    self.pop_candyParty()

                self.draw()

                now = datetime.datetime.today()

        if self._choiceLevel == 2:
            print("--- Début de la partie Difficile ---")

            self.draw()

            end = Game.end_time(1, 0)
            now = datetime.datetime.today()

            while now < end:
                self.player1.move()
                self.player2.move()
                if random.randint(1, 6) == 1:
                    self.check_candy_out_of_date()
                self.check_candy()
                self.check_Wall()

                i = 0
                while i != 3 :
                    self.enemy1.move()
                    self.enemy2.move()
                    self.check_Enemy()
                    self.check_candy()
                    self.check_Wall()
                    i = i + 1

                if random.randint(1, 3) == 1:
                    self.pop_candy()

                self.draw()

                now = datetime.datetime.today()

        elif self._choiceLevel == 3:
            print("--- Début de la partie Personalisé ---")

            self.draw()

            end = Game.end_time(self._min, self._sec)
            now = datetime.datetime.today()

            while now < end:
                self.player1.move()
                self.player2.move()
                if self._candyOutOfDateOrNot == 1 :
                    if random.randint(1, 6) == 1:
                        self.check_candy_out_of_date()
                self.check_candy()
                self.enemy1.move()
                self.enemy2.move()
                self.check_Enemy()
                self.check_candy()
                if self._wallPassOrNot == 1:
                    self.check_Position_TP()
                elif self._wallPassOrNot == 2:
                    self.check_Wall()

                if random.randint(1, 3) == 1:
                    self.pop_candy()

                if self._candyPartyOrNOT == 1 :
                    if self._candyPartyTrue == 1: #candyParty
                        self._candyPartyTrue = 0
                        self.pop_candyParty()

                self.draw()

                now = datetime.datetime.today()

        print("----- Terminé -----")
        print(self.player1._name, "vous avez", self.player1._points, "points")
        print(self.player2._name,"vous avez", self.player2._points, "points")
        self.storeLeaderBoard()
        #self.menu()

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
    e1 = Enemy((7,2))
    e2 = Enemy((7,7))
    g = Game(p1,p2,e1,e2)
    g.menu()




