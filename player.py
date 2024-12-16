# author: Amish Minocha
# class: CSE-30, PA#2
# date: October 12, 2022
# file: player.py: contains implementation of class Player and subclasses AI and MiniMax, with all the helper methods to execute functions.
# Functioning: Player class allows the user to choose a position, AI chooses a position based on random order, and MiniMax uses an algorithm that never loses.

from json.encoder import INFINITY
import random

class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X
    def get_sign(self):
        # return an instance sign
        return self.sign
    def get_name(self):
        # return an instance name
        return self.name
    def choose(self, board):
        # prompt the user to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.isempty(cell), and board.set(cell, sign)
        cell = input(self.name + ', ' + self.sign + ': Enter a cell [A-C][1-3]: ')
        cell = cell.lower()
        while(board.isempty(cell) != True or len(cell) != 2 or (cell[0] != 'a' and cell[0] != 'b' and cell[0] != 'c') or (cell[1] != '1' and cell[1] != '2' and cell[1] != '3')):
            print("\nYou did not choose correctly.")
            cell = input(self.name + ', ' + self.sign + ': Enter a cell [A-C][1-3]: ')
            cell = cell.lower()
        board.set(cell, self.sign)

class AI(Player):
    def __init__(self, name, sign, board):
        self.board = board
        super().__init__(name, sign)


    def choose(self, board):
        list_of_moves = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']
        list_of_moves_index = []
        for i in range(len(board.board)):
            if (board.board[i] == ' '):
                list_of_moves_index.append(i)
        cell = list_of_moves[random.choice(list_of_moves_index)]
        board.set(cell, self.sign)


class MiniMax(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)
    def choose(self, board):
        cell_list = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'] 
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        max_score = -100000000000
        best_move = 0
        for i in range(len(board.board)):
            if (board.board[i] == ' '):
                board.board[i] = self.sign
                score = MiniMax.minimax(self, board, False, True)
                if (score > max_score):
                    max_score = score
                    best_move = i
                board.board[i] = ' '
        cell = cell_list[best_move]
        print(cell)
        board.set(cell, self.sign)
        return
    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == '':
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1
                
        # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code 
        if self_player == True:
            max_score = -100000000000
            for i in range(len(board.board)):
                if (board.board[i] == ' '):
                    board.board[i] = self.sign
                    score = MiniMax.minimax(self, board, False, True)
                    if (score > max_score):
                        max_score = score
                    board.board[i] = ' '
            return max_score
        else:
            min_score = 100000000000
            for i in range(len(board.board)):
                if (board.board[i] == ' '):
                    board.board[i] = 'O'
                    score = MiniMax.minimax(self, board, True, True)
                    if (score < min_score):
                        min_score = score
                    board.board[i] = ' '
            return min_score     

