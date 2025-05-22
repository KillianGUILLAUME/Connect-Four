import numpy as np
import matplotlib.pyplot as plt

from plateau import Plateau

from strategy import Strategie


class Game0():
    def __init__(self):
        self.plateau = Plateau()
        self.board = self.plateau.getBoard()
        self.player=0
        self.historique = []

    def partie(self):
        nb_tour=0
        while True:
            self.plateau.afficherPuissance4()
            try:
                colonne = int(input("Joueur " + str(self.joueur +1) + " choisissez une colonne entre 0 et 6 :"))
                if 0<= colonne <= 6 :
                    if self.plateau.placer_pion(colonne)==True:
                        nb_tour+=1
                        print("Au tour " + str(nb_tour) + ", le joueur " + str(self.joueur +1) + " a placer son pion dans la colonne " + str(colonne + 1) + ".")
                        self.historique.append("Tour:" + str(nb_tour) + " /" + " joueur " + str(self.joueur + 1) + " /" + " colonne " + str(colonne))
                        print(self.board)
                        if self.plateau.regarder_victoire()==True:
                            print("Le joueur " + str(self.joueur + 1) + " a gagné la partie !")
                            print(self.historique)
                            self.plateau.afficherPuissance4()
                            break
                        elif self.plateau.nul()==True:
                            print("Aucun des deux joueurs n'a gagné la partie.")
                            print(self.historique)
                            break
                        else:
                            somme = self.joueur +1
                            self.joueur = somme%2
                    else:
                        print("La colonne est pleine, réessayez.")
                else:
                    print("La colonne doit être choisi entre 0 et 6.")
            except ValueError:
                print("Il faut mettre un NOMBRE comprit entre 0 et 6 !")


# game = Game0()
# game.partie()




class Game1():
    def __init__(self):
        self.plateau = Plateau()
        self.board = self.plateau.getBoard()
        self.joueur=0
        self.historique = []
        self.strat = Strategie(self.plateau)
        

    def partie(self):
        nb_tour=0
        while True:
            self.plateau.afficherPuissance4()
            if self.joueur + 1 == 1 :
                try:
                    colonne = int(input("Joueur " + str(self.joueur +1) + " choisissez une colonne entre 0 et 6 :"))
                    if 0<= colonne <= 6 :
                        if self.plateau.placer_pion(colonne)==True:
                            nb_tour+=1
                            print("Au tour " + str(nb_tour) + ", le joueur " + str(self.joueur +1) + " a placer son pion dans la colonne " + str(colonne + 1) + ".")
                            self.historique.append("Tour:" + str(nb_tour) + " /" + " joueur " + str(self.joueur + 1) + " /" + " colonne " + str(colonne))
                            print(self.board)
                            if self.plateau.regarder_victoire()==True:
                                print("Le joueur " + str(self.joueur + 1) + " a gagné la partie !")
                                print(self.historique)
                                self.plateau.afficherPuissance4()
                                break
                            elif self.plateau.nul()==True:
                                print("Aucun des deux joueurs n'a gagné la partie.")
                                print(self.historique)
                                break
                            else:
                                somme = self.joueur +1
                                self.joueur = somme%2
                        else:
                            print("La colonne est pleine, réessayez.")
                    else:
                        print("La colonne doit être choisi entre 0 et 6.")
                except ValueError:
                    print("Il faut mettre un NOMBRE comprit entre 0 et 6 !")
            else : #BOT
                nb_tour+=1

                position = self.strat.strategie1()
                self.plateau.matrice[position] = self.joueur + 1 
                print(self.board)

                print(f'le bot à joué {position},colonne : {position[1]}')
                self.historique.append("Tour:" + str(nb_tour) + " /" + " joueur " + str(self.joueur + 1) + " /" + " colonne " + str(position[1]))
                
                
                if self.plateau.regarder_victoire()==True:
                    print("Le bot a gagné la partie !")
                    print(self.historique)
                    self.plateau.afficherPuissance4()
                    break
                elif self.plateau.nul()==True:
                    print("Aucun des deux joueurs n'a gagné la partie.")
                    print(self.historique)
                    break
                else:
                    somme = self.joueur +1
                    self.joueur = somme%2
    

# game1 = Game1()
# game1.partie()



class Game2():
    def __init__(self):
        self.plateau = Plateau()
        self.board = self.plateau.getBoard()
        self.joueur=0
        self.historique = []
        self.strat = Strategie(self.plateau)
        

    def partie(self):
        nb_tour=0
        while True:
            self.plateau.afficherPuissance4()
            if self.joueur + 1 == 1 :
                try:
                    colonne = int(input("Joueur " + str(self.joueur +1) + " choisissez une colonne entre 0 et 6 :"))
                    if 0<= colonne <= 6 :
                        if self.plateau.placer_pion(colonne)==True:
                            nb_tour+=1
                            print("Au tour " + str(nb_tour) + ", le joueur " + str(self.joueur +1) + " a placer son pion dans la colonne " + str(colonne + 1) + ".")
                            self.historique.append("Tour:" + str(nb_tour) + " /" + " joueur " + str(self.joueur + 1) + " /" + " colonne " + str(colonne))
                            print(self.board)
                            if self.plateau.regarder_victoire()==True:
                                print("Le joueur " + str(self.joueur + 1) + " a gagné la partie !")
                                print(self.historique)
                                self.plateau.afficherPuissance4()
                                break
                            elif self.plateau.nul()==True:
                                print("Aucun des deux joueurs n'a gagné la partie.")
                                print(self.historique)
                                break
                            else:
                                somme = self.joueur +1
                                self.joueur = somme%2
                        else:
                            print("La colonne est pleine, réessayez.")
                    else:
                        print("La colonne doit être choisi entre 0 et 6.")
                except ValueError:
                    print("Il faut mettre un NOMBRE comprit entre 0 et 6 !")
            else : #BOT
                nb_tour+=1

                position = self.strat.strategie2()
                self.plateau.matrice[position] = self.joueur + 1 
                print(self.board)

                print(f'le bot à joué {position},colonne : {position[1]}')
                self.historique.append("Tour:" + str(nb_tour) + " /" + " joueur " + str(self.joueur + 1) + " /" + " colonne " + str(position[1]))
                
                
                if self.plateau.regarder_victoire()==True:
                    print("Le bot a gagné la partie !")
                    print(self.historique)
                    self.plateau.afficherPuissance4()
                    break
                elif self.plateau.nul()==True:
                    print("Aucun des deux joueurs n'a gagné la partie.")
                    print(self.historique)
                    break
                else:
                    somme = self.joueur +1
                    self.joueur = somme%2
    


# game2 = Game2()
# game2.partie()





class Game_minimax():
    def __init__(self):
        self.plateau = Plateau()
        self.board = self.plateau.getBoard()
        self.joueur=0
        self.historique = []
        self.strat = Strategie(self.plateau)
        

    def partie(self):
        nb_tour=0
        while True:
            self.plateau.afficherPuissance4()
            if self.joueur + 1 == 1 :
                try:
                    colonne = int(input("Joueur " + str(self.joueur +1) + " choisissez une colonne entre 0 et 6 :"))
                    if 0<= colonne <= 6 :
                        if self.plateau.placer_pion(colonne)==True:
                            nb_tour+=1
                            print("Au tour " + str(nb_tour) + ", le joueur " + str(self.joueur +1) + " a placer son pion dans la colonne " + str(colonne + 1) + ".")
                            self.historique.append("Tour:" + str(nb_tour) + " /" + " joueur " + str(self.joueur + 1) + " /" + " colonne " + str(colonne))
                            print(self.board)
                            if self.plateau.regarder_victoire()==True:
                                print("Le joueur " + str(self.joueur + 1) + " a gagné la partie !")
                                print(self.historique)
                                self.plateau.afficherPuissance4()
                                break
                            elif self.plateau.nul()==True:
                                print("Aucun des deux joueurs n'a gagné la partie.")
                                print(self.historique)
                                break
                            else:
                                somme = self.joueur +1
                                self.joueur = somme%2
                        else:
                            print("La colonne est pleine, réessayez.")
                    else:
                        print("La colonne doit être choisi entre 0 et 6.")
                except ValueError:
                    print("Il faut mettre un NOMBRE comprit entre 0 et 6 !")
            else : #BOT
                nb_tour+=1

                position = self.strat.strategie_minimax()
                self.plateau.matrice[position] = self.joueur + 1 
                print(self.board)

                # print(f'le bot à joué {position},colonne : {position[1]}')
                print(f'le bot à joué {position}')
                # self.historique.append("Tour:" + str(nb_tour) + " /" + " joueur " + str(self.joueur + 1) + " /" + " colonne " + str(position[1]))
                self.historique.append("Tour:" + str(nb_tour) + " /" + " joueur " + str(self.joueur + 1) + " /" + " colonne " + str(position))

                
                if self.plateau.regarder_victoire()==True:
                    print("Le bot a gagné la partie !")
                    print(self.historique)
                    self.plateau.afficherPuissance4()
                    break
                elif self.plateau.nul()==True:
                    print("Aucun des deux joueurs n'a gagné la partie.")
                    print(self.board)
                    print(self.historique)
                    break
                else:
                    somme = self.joueur +1
                    self.joueur = somme%2
    




gameminimax = Game_minimax()
gameminimax.partie()
