'''
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

4 kyu Snail

Given an n x n array, return the array elements arranged from outermost
elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array
consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

note: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.
note 2: The 0x0 (empty matrix) is represented as en empty array inside an
array [[]].
'''


import numpy as np  # used in the second function


def snail(snail_map):
    rowstart = colstart = 0
    rowend = len(snail_map) - 1
    colend = len(snail_map[0]) - 1
    result = []

    while rowstart <= rowend and colstart <= colend:
        for i in range(colstart, colend + 1):
            result.append(snail_map[rowstart][i])
        rowstart += 1

        for i in range(rowstart, rowend + 1):
            result.append(snail_map[i][rowend])
        colend -= 1

        if rowstart <= rowend:
            for i in range(colend, colstart - 1, -1):
                result.append(snail_map[rowend][i])
        rowend -= 1

        if colstart <= colend:
            for i in range(rowend, rowstart - 1, -1):
                result.append(snail_map[i][colstart])
        colstart += 1

    return result


# This is one of the best practices - voted in codewars
def snail2(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(snail2(array), expected)

array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(snail(array), expected)
