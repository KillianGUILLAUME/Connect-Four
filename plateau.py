import numpy as np
import matplotlib.pyplot as plt


class Plateau:
    def __init__(self):
        self.tailleMap = (6,7)
        self.matrice=np.zeros(self.tailleMap)
        self.joueur = 0
        

    def afficherPuissance4(self):
        plt.figure(figsize=(7, 6))
        plt.grid(True, color='blue', linestyle='-')
        ax = plt.gca()
        ax.set_xlim([0, 7])
        ax.set_ylim([0, 6])
        for x in range(7):
            for y in range(6):
                if self.matrice[5 - y,x] == 1:
                    plt.scatter(x + 0.5, y + 0.5, color='r', s=1300)
                elif self.matrice[5 - y,x] == 2:
                    plt.scatter(x + 0.5, y + 0.5, color='y', s=1300)
        plt.show()


    def placer_pion(self,colonne):
        for i in range(6):
            if self.matrice[5-i][colonne]==0:
                self.matrice[5-i][colonne] = self.joueur +1
                return True


    def regarder_victoire(self):
        # victoire horizontal
        for c in range(4):
            for l in range(6):
                if self.matrice[l,c] == self.joueur+1 and self.matrice[l,c + 1] == self.joueur+1 and self.matrice[l,c + 2] == self.joueur+1 and self.matrice[l,c + 3] == self.joueur+1:
                    return True
        # victoire verticale
        for c in range(7):
            for l in range(3):
                if self.matrice[l,c] == self.joueur+1 and self.matrice[l + 1,c] == self.joueur+1 and self.matrice[l + 2,c] == self.joueur+1 and self.matrice[l + 3,c] == self.joueur+1:
                    return True
        # victoire diagonale droite en haut
        for c in range(4):
            for l in range(3):
                if self.matrice[5 - l,c] == self.joueur+1 and self.matrice[4 - l,c + 1] == self.joueur+1 and self.matrice[3 - l,c + 2] == self.joueur+1 and self.matrice[2 - l,c + 3] == self.joueur+1:
                    return True
        # victoire diagonale droite en bas
        for c in range(4):
            for l in range(3):
                if self.matrice[l,c] == self.joueur+1 and self.matrice[l + 1,c + 1] == self.joueur+1 and self.matrice[l + 2,c + 2] == self.joueur+1 and self.matrice[l + 3,c + 3] == self.joueur+1:
                    return True


    def nul(self):
        if self.matrice[0,0]!=0 and self.matrice[0,0]!=0 and self.matrice[0,2]!=0 and self.matrice[0,3]!=0 and self.matrice[0,4]!=0 and self.matrice[0,5]!=0 and self.matrice[0,6]!=0:
            return True
        
    def getBoard(self):
        return self.matrice
    
    def getTailleMap(self):
        return self.tailleMap
        