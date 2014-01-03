#Sudoku-Solver by Evan Fossier
#Last Updated 1/2/2014

from Sudoku import Sudoku
import copy
import sys
import time

test = [[None,None,None,None,None,8,None,None,4],
        [None,8,4,None,1,6,None,None,None],
        [None,None,None,5,None,None,1,None,None],
        [1,None,3,8,None,None,9,None,None],
        [6,None,8,None,None,None,4,None,3],
        [None,None,2,None,None,9,5,None,1],
        [None,None,7,None,None,2,None,None,None],
        [None,None,None,7,8,None,2,6,None],
        [2,None,None,3,None,None,None,None,None]]
        
extreme = [[4,None,None,5,None,None,None,None,1],
            [None,None,1,None,3,None,None,9,None],
            [None,7,9,None,None,4,None,None,None],
            [3,None,None,None,None,6,7,None,None],
            [None,4,None,None,7,None,None,8,None],
            [None,None,6,4,None,None,None,None,9],
            [None,None,None,3,None,None,8,1,None],
            [None,3,None,None,9,None,5,None,None],
            [6,None,None,None,None,5,None,None,2]]
            
examples = {'test':test, 'extreme':extreme}

num_boards = 0 #global variable to keep track of number of complete boards encountered during algorithm

def solve(board):
    #recursively called on a board until a solution is found
    #on each call, tries certain values at the next empty spot, checks if the board is correct, if not finished, recursively calls itself on children boards
        
    index = board.next_empty() #next empty cell in tuple of form (row,col)
    global num_boards
    if index != None: #board is not yet completed
        invalid_nums = board.get_row_as_set(index[0]) | board.get_col_as_set(index[1]) #do union operation
        square_num = (index[0] // 3) * 3 + (index[1] // 3) #get the square containing this index
        invalid_nums = invalid_nums.union(board.get_square_as_set(square_num))
        possible = set(range(1,10)).difference(invalid_nums) #legal values for this spot
        if len(possible) == 0: #no possible values so board cannot be solved
            num_boards += 1
            return None
        for i in possible:
            new_board = copy.deepcopy(board)
            new_board.set_val(i, index[0],index[1])
            solution = solve(new_board)
            if solution == None:
                continue
            else:
                return solution
        return None
    else:
        if board.is_correct():
            return board
        else:
            num_boards += 1
            return None
            
def main():
    print('Sudoku Solver 1.0')
    if '-help' in sys.argv:
        print("Sudoku Solver written by Evan Fossier")
        print("Last updated 1/2/2014")
        print("Flags:")
        print("\t-t: activates timer functionality, returns its run time in s")
        print("\t-p: enter the sudoku board as a single python list")
        print("\t-f filename: select a file to output the solution board")
        print("\t-s: return number of boards tried")
        print("\t-ex: run on example boards (2)")
        print("\tdefault: input the sudoku board line by line")
        return
    if '-t' in sys.argv:
        print('Timer function enabled')
        
    if '-p' in sys.argv: #python list mode
        board = handle_p()
        if board != None:
            board = Sudoku(board)
        else:
            return
    elif '-ex' in sys.argv: #use example boards
        print("Available examples:")
        for ex in examples.keys():
            print(ex)
            print(Sudoku(examples[ex]))
            print("\n")
        
        board = input("Type in name of example board to solve:")
        try:
            board = examples[board]
            board = Sudoku(board)
        except:
            print("Couldn't find that board")
            return
    else:
        board = handle_input()
        board = Sudoku(board)
        
    if '-f' in sys.argv:
        index = sys.argv.index('-f')
        filename = sys.argv[index+1]
        try:
            f = open(filename, 'w')
        except:
            print('Problem opening %s' % filename)
        print('Outputing to %s' % filename)
        sys.stdout = f
    
    global num_boards
    num_boards = 0
    
    print('\nboard to solve:')
    print(board)
    start = time.clock()
    sol = solve(board)
    end = time.clock() - start
    print('solution:')
    print(sol)
    if '-t' in sys.argv:
        print('Time:'+str(end)+' s')
    if '-s' in sys.argv:
        print('Num boards tried: %d' % num_boards)
    return
    
def handle_p():
    print('Enter a board as a python list where each element is itself a list of the values in that row')
    print('Use None to indicate an empty spot')
    print('This method does not check list for integrity...')
    print('Make sure everything is on the same line')
    try:
        board = eval(input('Input a board (python list): '))
    except:
        print("Invalid board")
        return None
    if type(board) != list or len(board) != 9:
        print('Invalid board')
        return None
    return board

def handle_input():
    print("Enter the board line by line with spaces separating each value, enter x for an empty cell")
    print("Alternatively you can enter the row without spaces")
    print("Type 'exit' to immediately quit")
    board = []
    i = 1
    while True:
        row = input('Row %d:' % i)
        if row == 'exit':
            return #emergency exit prompt
        row = row.split()
        invalid = False
        
        if (len(row) != 9) and (len(row) != 1):
            invalid = True
        else:
            if len(row) == 1:#entered without spaces
                row = row[0]
                if len(row) != 9: invalid = True
                
            if not invalid:
                for x in range(0,9):
                    if row[x] == 'x': #empty cell placeholder
                        row[x] = None
                    else:
                        try:
                            row[x] = int(row[x]) #entry is an int
                            if row[x] <= 0 or row[x]>=10:
                                invalid = True
                        except:
                            invalid = True #entry is something else
        if not invalid:
            board.append(row)
            i += 1
            if i == 10:
                break #done entering board
        else:
            print("Invalid Row")
            continue
    return board
    
if __name__ == '__main__':  
    main()
