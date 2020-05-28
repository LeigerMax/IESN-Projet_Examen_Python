# ExamenPython2020
## Explication du jeu 
Il s’agit d’un petit jeu de plateau (de 10 cases par défaut) sur lequel un joueur se déplace et doit
récupérer des bonbons qui apparaissent aléatoirement. Le joueur à une minute pour en récolter le
plus possible.
Quand on ramasse un bonbon, il se peut que ce bonbon soit magique, les bonbons magiques font spawn entre 1 et 5 bonbons.
Dans le jeu de base nous avons deux ennemis qui se balade aléatoirement sur la carte, une fois que celui-ci touche un bonbon, le bonbon est mangé. Si l'ennemi touche un joueur celui-ci perd 2 points. Si le joueur toucher à plus de 10 points, il perd tous ses points !


## Tache à faire 
- [X] Empêcher le joueur de revenir en arrière [1]
- [x] Ajouter un second joueur [3] 
- [x] Ajouter des ennemis qui se déplacent aléatoirement [2]
- [x] Donner des valeurs différentes aux bonbons récoltés (éventuellement malus) [1] 
- [x] Ajouter des bonbons bonus (par exemple faire apparaitre pleins de bonbons) [2]
- [X] Encapsuler les classes [1]
- [X] Utiliser des exceptions [2]
- [ ] Permettre de mettre le jeu en pause [3]
- [X] Améliorer les ennemis en leur donnant un peu d’intelligence (IA) [2]
- [X] Proposer un niveau de difficulté différent (plus de temps, des pénalités…) [2]
- [X] Empêcher de sortir du plateau [1]
- [X] Permettre de passer à travers les murs et de réapparaitre de l’autre côté [2]
- [X] Enregistrer les tops joueurs [1] (dans un fichier [3]) et l'afficher via le jeu
- [ ] Améliorer le jeu pour en faire un snake [4]
- [X] Mettre des couleurs (Fonctionne que avec PyCharm)
- [X] Bonbon avec malus
- [X] Mode normal, difficile , personnalisé
- [X] Permettre de se rendre sur le gihub.
- [X] Afficher le Readme en jeu

## Player
La Classe Player permet de créer des joueurs, elle permet de gérer les déplacements, les points et les noms des joueurs.
## Enemy
La Classe Enemy permet de créer des ennemis, elle permet de gérer les déplacements de ceci de manière aléatoire.
## Game
La Classe Game permet de lancer le jeu.
### draw
Permet de dessiner le plateau de jeu, le plateau fait 10*10. Il dessine également murs qui entoure le plateau, les bonbons, les joueurs et les ennemis.
### pop_candy 
Fait apparaitre un bonbon dans une position random dans le plateau.
### pop_candyParty 
La fonction ici permet de choisir entre 1 et 5 bonbon(s) random qui vont apparaitre sur le plateau.
### check_candy
Cette fonction regarde s'il y a un bonbon à prendre et le prend s'il en a un. En le prenant les joueurs peuvent gagner des points, entre 1 et 3. Si c'est un ennemi qui le prend, il sera détruit. Il permet également de choisir si un bonbon est magique ou pas.
### check_candy_out_of_date
Permet de retirer 5 points si le joueur tombe sur un bonbon périmé.
### check_Position_TP
Cette fonction permet de passer à travers les murs et de réapparaitre de l’autre côté. Elle fonctionne pour les deux joueurs et les ennemis.
### check_Wall
La fonction permet de bloquer les joueurs et les ennemis quand ils tentent de traverser un mur.
### check_Enemy
Cette fonction permet de vérifier si un ennemi touche un joueur ou pas. S"il le touche il lui enlève 2 points. Si le joueur à plus de 10 points l'ennemi lui prendra tous ses points.
### storeLeaderBoard
Permet d'enregistrer le score des joueurs dans un fichier.
### displayLeaderboard
Permet d'ouvrir le fichier qui contient les scores et l'afficher.
### displayReadme
Affiche le ficher Readme.
### Menu
Permet de créer un menu dès le lancement du jeu. Il affiche différente option de lancement : 
  * Normal (1) : 1 minute, 2 ennemis, mur bloquer et bonbon magique.
  * Difficile (2) : 1 minute, 2 ennemis avec 3 mouvements, moins de spawn de bonbon, bonbon périmé.
  * Personnalisé  (3) : Permet de personnaliser  sa partie comme le joueur souhaite. 
  * Tableau des score (4) : Afficher le tableau des scores.
  * Afficher le Readme (5) : Affiche le fichier Readme.
  * GitHub du projet (6) : Affiche le github du projet.
### play
Permet de lancer le jeu par rapport aux paramètres que nous avons choisis.
### end_time
Retourne le moment où le jeu est censé être fini
