'''
https://www.codewars.com/kata/5e28b3ff0acfbb001f348ccc/python

7 kyu Sliding Puzzle Verification

Description: Given a board of NxN, distributed with tiles labeled 0 to N² -
1(inclusive):

A solved grid will have the tiles in order of label, left to right, top to
bottom.

Return true if the board state is currently solved, and false if the board
state is unsolved.

Input will always be a square 2d array.

For example, a 2x2 solved grid:

[ [0, 1],
  [2, 3] ]
A 2x2 unsolved grid:

[ [2, 1],
  [0, 3] ]
'''


def is_solved(board):
    b = []
    for i in board:
        b.append(sorted(i))
    return board == sorted(b)


def is_solved2(board):
    board = sum(board, [])
    return board == sorted(board)


print(is_solved([[0, 1], [2, 3]]))  # True)
print(is_solved([[1, 0], [3, 2]]))  # False)
print(is_solved2([[0, 1], [2, 3]]))  # True)
print(is_solved2([[1, 0], [3, 2]]))  # False)
