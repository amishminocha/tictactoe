# author: Amish Minocha
# class: CSE-30, PA#2
# date: October 12, 2022
# file: board.py: contains implementation of class Board with all the helper methods to execute functions.
# Initialization of object: Creates a list with empty cells.

class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""
    def get_size(self): 
            # optional, return the board size (an instance size)
        size = 0
        for i in self.board:
            if (i != ' '):
                size+=1
        return size
    def get_winner(self):
        # return the winner's sign O or X (an instance winner)     
        return self.winner
    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can use a tuple ("A1", "B1",...) to obtain indexes 
        # this implementation is up to you 
        if (cell == 'a1'):
            self.board[0] = sign
        if (cell == 'b1'):
            self.board[1] = sign
        if (cell == 'c1'):
            self.board[2] = sign
        if (cell == 'a2'):
            self.board[3] = sign
        if (cell == 'b2'):
            self.board[4] = sign
        if (cell == 'c2'):
            self.board[5] = sign
        if (cell == 'a3'):
            self.board[6] = sign
        if (cell == 'b3'):
            self.board[7] = sign
        if (cell == 'c3'):
            self.board[8] = sign
    def isempty(self, cell):
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # return True if the cell is empty (not marked with X or O)
        if (cell == 'a1' and self.board[0] == ' '):
            return True
        if (cell == 'b1' and self.board[1] == ' '):
            return True
        if (cell == 'c1' and self.board[2] == ' '):
            return True
        if (cell == 'a2' and self.board[3] == ' '):
            return True
        if (cell == 'b2' and self.board[4] == ' '):
            return True
        if (cell == 'c2' and self.board[5] == ' '):
            return True
        if (cell == 'a3' and self.board[6] == ' '):
            return True
        if (cell == 'b3' and self.board[7] == ' '):
            return True
        if (cell == 'c3' and self.board[8] == ' '):
            return True

    def isdone(self):
        done = False
        self.winner = ''
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        mytuple = tuple(self.board)
        a1, b1, c1, a2, b2, c2, a3, b3, c3 = mytuple
        if (self.board[0: 3] == ['X', 'X', 'X'] or self.board[3: 6] == ['X', 'X', 'X'] or self.board[6:] == ['X', 'X', 'X']):
            done = True
            self.winner = 'X'
        elif (self.board[0: 3] == ['O', 'O', 'O'] or self.board[3: 6] == ['O', 'O', 'O'] or self.board[6:] == ['O', 'O', 'O']):
            done = True
            self.winner = 'O'
        elif ((a1 == 'X' and a2 == 'X' and a3 == 'X') or (b1 == 'X' and b2 == 'X' and b3 == 'X') or (c1 == 'X' and c2 == 'X' and c3 == 'X')):
            done = True
            self.winner = 'X'
        elif ((a1 == 'O' and a2 == 'O' and a3 == 'O') or (b1 == 'O' and b2 == 'O' and b3 == 'O') or (c1 == 'O' and c2 == 'O' and c3 == 'O')):
            done = True
            self.winner = 'O'
        elif ((a1 == 'X' and b2 == 'X' and c3 == 'X') or (c1 == 'X' and b2 == 'X' and a3 == 'X')):
            done = True
            self.winner = 'X'
        elif ((a1 == 'O' and b2 == 'O' and c3 == 'O') or (c1 == 'O' and b2 == 'O' and a3 == 'O')):
            done = True
            self.winner = 'O'
        try:
            mytuple.index(' ')
        except:
            done = True
        return done
    def show(self):
        # draw the board
        print('\n   A   B   C ')
        print(' +---+---+---+')
        print('1| ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2] + ' |')
        print(' +---+---+---+')
        print('2| ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5] + ' |')
        print(' +---+---+---+')
        print('3| ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8] + ' |')
        print(' +---+---+---+')