#Part of Sudoku-Solver by Evan Fossier
#Last updated 1/2/2014
#This file contains the definition for a 9x9 Sudoku board
#Board may be complete or incomplete

class Sudoku():

    def __init__(self, board):
        self.board = board #board is 2-d array representing a 9x9 sudoku grid where self.board[row][col]
        self.correct = None #don't know if the board is correct yet
    
    def __str__(self):
        k = 1
        string = ''
        for row in self.board:
            i = 0
            for item in row:
                if i == 3:
                    string += '| '
                    i = 0
                    
                if item == None: #empty cell
                    string += 'x '
                else:
                    string += str(item) + ' '
                i += 1
            string += '\n'
            if (k % 3 == 0) and (k != 9):
                string += '- - - - - - - - - - - \n'
            k += 1
        return string
         
    def is_correct(self):
        #return True if this board is correct, False otherwise
        if self.correct != None:
            return self.correct #return cached result if possible
        correct = True
        for i in range(0,9):
            row = self.get_row_as_set(i)
            col = self.get_col_as_set(i)
            square = self.get_square_as_set(i)
            if (len(row) == 9) and (len(col) == 9) and (len(square) == 9):
                #all sets must hold 9 unique values
                continue
            else:
                correct = False
                break
        self.correct = correct #cache result
        return correct
        
    def set_val(self, val, row, col):
        #sets self.board[row][col] to val
        assert 0 < val <= 9, 'Invalid value'
        assert 0 <= row < 9, 'Invalid row'
        assert 0 <= col < 9, 'Invalid column'
        self.board[row][col] = val
        
    def get_row_as_set(self, row_index):
        #returns the row at row_index in set format (no duplicate values)
        vals = set()
        for i in self.board[row_index]:
            if i != None:
                vals.add(i)
        return vals
        
    def get_col_as_set(self, col_index):
        #returns the column at col_index in set format
        vals = set()
        for row in self.board:
            i = row[col_index]
            if i != None:
                vals.add(i)
        return vals
        
    def get_square_as_set(self, n):
        #Squares are numbered 0-8 from left to right, top to bottom
        #returns a set containing the values of the nth square.
        col_indexes = (n % 3) * 3 #start index of the columns to go through
        row_indexes = (n // 3) * 3 #start index of rows to go through
        vals = set()
        for i in range(row_indexes, row_indexes+3):
            cur_row = self.board[i]
            for j in range(col_indexes, col_indexes+3):
                item = cur_row[j]
                if item != None:
                    vals.add(item)
        return vals
        
    def next_empty(self):
        #returns tuple (row,col) of next empty spot in this board
        for i in range(0,9):
            cur_row = self.board[i]
            for j in range(0,9):
                if cur_row[j] == None:
                    return (i,j)
        return None
