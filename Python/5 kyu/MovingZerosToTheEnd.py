'''
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

5 kyu Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

'''

# def move_zeros(array):
#     zeros = array.count(0)
#     while 0 in array:
#         array.remove(0)
#     array.extend([0 for i in range(zeros)])
#     return array


def move_zeros(array):
    zero = list(filter(lambda a: a == 0 and not isinstance(a, bool), array))
    return list(filter(lambda a: a != 0 or isinstance(a, bool), array)) + zero


print(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [],
                 0, 1, 9, 0, 0, {}, 0, 0, 9]))
# ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {},
# 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print(move_zeros([0, 1, None, 2, False, 1, 0]))
# [1, None, 2, False, 1, 0, 0]

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
# [ 1,  2,  1,  1,  3,  1,  0,  0,  0,  0 ])

print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1,
                  0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
# [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0,
                  1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
# ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print(move_zeros(["a",  "b"]))  # ["a", "b"])

print(move_zeros(["a"]))  # ["a"])

print(move_zeros([0,  0]))  # [0, 0])

print(move_zeros([0]))  # [0])

print(move_zeros([False]))  # [False])

print(move_zeros([]))  # [])
