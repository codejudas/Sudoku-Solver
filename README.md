Sudoku-Solver
=============

Simple Sudoku Solver written in Python as a side project over my winter break.
The program basically takes a 9x9 Sudoku board as input and attempts every legal move in the next open cell until either the board is complete and correct, there are no more legal moves in the next space, or the board is complete and is a dead end.

Input
=====

By default (no flags), the program will prompt the user to enter the sudoku board row by row. This is the prefered method to enter a board. The program will verify that each row is correct before moving on to the next one.

The program will also take the sudoku board as a 2d row-major python list (use the -p flag). This method is cumbersome and there is very little error checking for the input list.

Output
======

The program can either output to the console in which this is run, or alternatively output to a file specified after the -f flag.

Installation
============
Download Solver.py and Sudoku.py and place them anywhere on your computer

You must have Python 3+ installed on your computer, this may work on Python 2.7 but I have no tested it.
To run, type this into your console:

python Solver.py [-flags]

Options
=======
You can specify several command line options when running the solver. By default the program will prompt you to enter the board row by row. Other options are:

  -t: activates timer functionality, times program execution and prints result in seconds
  
  -p: program will instead prompt you to enter a 2d python list in row major form of the board. Everything must be entered on a single line.
  
  -f filename: outputs the solution to 'filename'
  
  -s: program will keep track of how many complete boards it has tried before finding the correct solution.
  
  -ex: prints example boards included in Solver.py (there are 2) and allows you to select one and solve it.
  
License
=======
You are welcome to use any part of this project or improve on it in any way you like without asking me.
