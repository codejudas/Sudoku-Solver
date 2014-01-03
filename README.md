Sudoku-Solver
=============

Simple Sudoku Solver written in Python as a side project over winter break.
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

You must have Python 3+ installed on your computer, this may work on Python 2.7 but I have no tested it.
To run, type this into your console:

python Solver.py [-flags]
