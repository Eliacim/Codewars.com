# https://www.codewars.com/kata/5e28b3ff0acfbb001f348ccc/solutions/python

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
