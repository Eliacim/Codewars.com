"""

5 kyu
Land perimeter

https://www.codewars.com/kata/5839c48f0cf94640a20001d3

Task:
Given an array arr of strings complete the function landPerimeter by
calculating the total perimeter of all the islands. Each piece of land will be
marked with 'X' while the water fields are represented as 'O'. Consider each
tile being a perfect 1 x 1piece of land. Some examples for better
visualization:


['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']

should return: "Total land perimeter: 24",


['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']

should return: "Total land perimeter: 18"

"""


def land_perimeter(arr):
    i = 0
    rows = len(arr)
    columns = len(arr[0])
    for r in range(rows):
        for c in range(columns):
            if arr[r][c] == "X":
                i += 4
                i -= 1 if (r != rows - 1) and (arr[r + 1][c] == "X") else 0
                i -= 1 if (r != 0) and (arr[r - 1][c] == "X") else 0
                i -= 1 if (c != columns - 1) and (arr[r][c + 1] == "X") else 0
                i -= 1 if (c != 0) and (arr[r][c - 1] == "X") else 0
    result = "Total land perimeter: %i" % i
    print(result)
    return result


assert land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX",
                       "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]) ==\
                           "Total land perimeter: 60"

assert land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO",
                       "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]) ==\
                           "Total land perimeter: 52"

assert land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO",
                       "XXXOOOXO", "OXOXXOOX"]) ==\
                           "Total land perimeter: 40"

assert land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO",
                       "OOOOOXX", "OOOXOXX", "XXXXOXO"]) ==\
                           "Total land perimeter: 54"

assert land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO",
                       "OOOOOO", "OOOXOO", "OOXXOO"]) ==\
                           "Total land perimeter: 40"
