'''
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

4 kyu Range Extraction

A format for expressing an ordered list of integers is to use a comma separated
list of either

individual integers or a range of integers denoted by the starting integer
separated from the end integer in the range by a dash,  '-'. The range includes
all integers in the interval including both endpoints. It is not considered a
range unless it spans at least 3 numbers. For example ("12,  13,  15-17")
Complete the solution so that it takes a list of integers in increasing order
and returns a correctly formatted string in the range format.

Example:

solution([-6,  -3,  -2,  -1,  0,  1,  3,  4,  5,  7,  8,  9,  10,  11,  14,
15,  17,  18,  19, 20])
# returns "-6, -3-1, 3-5, 7-11, 14, 15, 17-20"
'''


def solution(args):
    tmp = final = 0
    result = []

    for i in range(0, len(args)):
        if i == len(args) - 1:
            tmp = 1
        elif args[i] + 1 == args[i + 1]:
            final += 1
        else:
            tmp = 1
        
        if tmp == 1 and final == 0:
            result.append(str(args[i]))
            tmp = 0
        elif tmp == 1 and final > 1:
            result.append(str(args[i] - final) + "-" + str(args[i]))
            tmp = final = 0
        elif tmp == 1 and final == 1:
            result.append(str(args[i] - final))
            result.append(str(args[i]))
            tmp = final = 0

    return ','.join(res for res in result)


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14,
               15, 17, 18, 19, 20]))
# '-6, -3-1, 3-5, 7-11, 14, 15, 17-20'

print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
# '-3--1, 2, 10, 15, 16, 18-20'
