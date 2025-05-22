import numpy as np
import random
import math

from plateau import Plateau
from copy import copy



def check_victory(matrice,joueur):
    # victoire horizontal
    for c in range(4):
        for l in range(6):
            if matrice[l,c] == joueur+1 and matrice[l,c + 1] == joueur+1 and matrice[l,c + 2] == joueur+1 and matrice[l,c + 3] == joueur+1:
                return True
    # victoire verticale
    for c in range(7):
        for l in range(3):
            if matrice[l,c] == joueur+1 and matrice[l + 1,c] == joueur+1 and matrice[l + 2,c] == joueur+1 and matrice[l + 3,c] == joueur+1:
                return True
    # victoire diagonale droite en haut
    for c in range(4):
        for l in range(3):
            if matrice[5 - l,c] == joueur+1 and matrice[4 - l,c + 1] == joueur+1 and matrice[3 - l,c + 2] == joueur+1 and matrice[2 - l,c + 3] == joueur+1:
                return True
    # victoire diagonale droite en bas
    for c in range(4):
        for l in range(3):
            if matrice[l,c] == joueur+1 and matrice[l + 1,c + 1] == joueur+1 and matrice[l + 2,c + 2] == joueur+1 and matrice[l + 3,c + 3] == joueur+1:
                return True



def getNeighborhood(board):
    L = board.shape[0] - 1
    C = board.shape[1] - 1

    liste_neighbors = []
    for colonne in range(C+1):
        for ligne in range(L):
            if board[L -ligne, colonne] == 0:
                liste_neighbors.append((L - ligne, colonne))
                break
    return liste_neighbors



def terminal_node(board,joueur):
    return check_victory(board,joueur) or check_victory(board,joueur - 1)







class Strategie():
    def __init__(self,plateau):

        self.plateau = plateau
        self.board = self.plateau.getBoard()
        self.L=self.plateau.getTailleMap()[0] -1
        self.C=self.plateau.getTailleMap()[1] -1
        self.joueur = 2


    def strategie1(self):
        board_copy = self.board.copy()
        ln = getNeighborhood(board_copy)
        print(ln)
        for position in ln:
            board_copy[position] = self.joueur

            if check_victory(board_copy,self.joueur-1)==True:
                print("j'ai repéré cette condition de victoire")
                return position
            
            else:
                board_copy[position]=0
        
        for position in ln:

            board_copy[position] = self.joueur -1
            if check_victory(board_copy,self.joueur-2)==True:

                print("j'ai empéché cette condition de victoire")
                return position
            else :
                board_copy[position]=0

        
        return random.choice(ln)


    def strategie2(self):
        path = []

        board_copy = self.board.copy()
        ln = getNeighborhood(board_copy)
        
        for position in ln:
            board_copy[position] = self.joueur

            if check_victory(board_copy,self.joueur-1)==True:
                print("j'ai repéré cette condition de victoire")
                return position
            
            else:
                board_copy[position]=0
        
        for position in ln:

            board_copy[position] = self.joueur -1
            if check_victory(board_copy,self.joueur-2)==True:

                print("j'ai empéché cette condition de victoire")
                return position
            else :
                board_copy[position]=0

        for position in ln:

            board_copy[position] = self.joueur
            path.append(position)
            board_copy_adv = self.board.copy()
            ln_adv = getNeighborhood(board_copy_adv)

            for pos_adv in ln_adv:
                board_copy_adv[pos_adv] = self.joueur - 2
                if check_victory(board_copy_adv,self.joueur-2)==True:
                    print(f'ne pas utiliser ce chemin, win en 1 pour {self.joueur - 1}')
                    board_copy_adv[pos_adv] = 0
                    path.pop()

        if len(path) > 0 :
            return random.choice(path)
        else :
            print('Bien joué !')
            return random.choice(ln)
        
        
    def strategie_minimax(self, depth=3):
        algo = Minimax(self.board.copy(), self.joueur)
        best_pos = algo.minimax(self.board.copy(), depth, -math.inf, math.inf, True)[0]
        print(f'ici best pos : {best_pos}')
        return best_pos




class Minimax():
    def __init__(self, board, joueur):
        # board = board
        self.joueur = joueur
        self.L=board.shape[0] 
        self.C=board.shape[1] 



    def give_score(self,player,board):
        score = 0

        # Priorité au centre
        center_col = board[:, self.C // 2]
        center_count = list(center_col).count(player)
        score += center_count * 3

        def evaluate_window(window):
            score = 0
            opponent = 3 - player

            def consecutive(window, number,count):
                # number : IdPlayer
                streak = 0
                for val in list(reversed(window)):
                    if val == number:
                        streak += 1
                        if streak == count:
                            return True
                    else:
                        streak = 0
                return False

            

            if consecutive(window, player, 4):
                score += 100000
            elif consecutive(window, player, 3):
                score += 1000
            elif consecutive(window, player, 2):
                score += 100

            elif consecutive(window, opponent, 3):
                score +=1000

            return score

        # Vérifie toutes les fenêtres de 4 horizontalement
        for l in range(self.L):
            for c in range(self.C - 3):
                window = list(board[l, c:c+4])
                score += evaluate_window(window)

        # Vertical
        for c in range(self.C):
            for l in range(self.L - 3):
                window = list(board[l:l+4, c])
                score += evaluate_window(window)

        # Diagonale haut-droite
        for l in range(self.L - 3):
            for c in range(self.C - 3):
                window = [board[l+i, c+i] for i in range(4)]
                score += evaluate_window(window)

        # Diagonale bas-droite
        for l in range(3, self.L):
            for c in range(self.C - 3):
                window = [board[l-i, c+i] for i in range(4)]
                score += evaluate_window(window)

        return score
    

    def minimax(self, board ,depth, alpha, beta, maximizingPlayer):


        score = self.give_score(maximizingPlayer,board)

        valid_locations = getNeighborhood(board)
        terminal = terminal_node(board,self.joueur)

        if depth == 0 or terminal:
            if terminal:
                if check_victory(board, self.joueur - 1):
                    return (None, 100000000000)
                elif check_victory(board, self.joueur - 2):
                    return (None, -100000000000)
                else:
                    return (None, 0)
            else:
                return (None, score)
            
        

    # for d in range(depth):

    #     b_copy = board.copy()
    #     b_copy[position] = self.joueur
    #     new_score = self.minimax(b_copy, depth-d, alpha, beta, False)[1]














        if maximizingPlayer:
            value = -math.inf
            # best_pos = random.choice(valid_locations)
            best_pos = None


            for position in valid_locations:
                b_copy = board.copy()
                b_copy[position] = self.joueur
                new_score = self.minimax(b_copy, depth-1, alpha, beta, False)[1]
                print(f' new score = {new_score}, player = {maximizingPlayer}')
                if new_score > value:
                    value = new_score
                    best_pos = position
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            print(board)
            print(best_pos,value,maximizingPlayer)
            return best_pos, value

        else:
            value = math.inf
            best_pos = None
            for position in valid_locations:
                b_copy = board.copy()
                b_copy[position] = self.joueur - 1
                new_score = self.minimax(b_copy, depth-1, alpha, beta, True)[1]
                print(f' new score = {new_score}')
                if new_score < value:
                    value = new_score
                    best_pos = position
                beta = min(beta, value)
                if alpha >= beta:
                    break
            print(board)
            print(best_pos,value)
            return best_pos, value





    

