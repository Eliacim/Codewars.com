'''
https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

5 kyu Sum of Pairs

Sum of Pairs
Given a list of integers and a single sum value, return the first two values
(parse from the left please) in order of appearance that add up to form the sum
Negative numbers and duplicate numbers can and will appear.

There will also be lists tested of lengths upwards of 10,000,000 elements.
Be sure your code doesn't time out.
'''


# First tempative, works but in the final test took more than 12s :(
def sum_pairs1(ints, s):
    pastitem = set()
    for e, i in enumerate(ints):
        for r in range(e + 1, len(ints)):
            if (i + ints[r]) == s:
                return [i, ints[r]]
            for past in pastitem:
                if (past + ints[r]) == s:
                    return [past, ints[r]]
            pastitem.add(ints[r])
            print(pastitem)


# This is the a faster one that works perfectly!
def sum_pairs(ints, s):
    pastitems = set()
    for i in ints:
        if s - i in pastitems:
            return [s - i, i]
        pastitems.add(i)


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 9, 5, 5, 10, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

print(sum_pairs(l1, 8) == [1, 7],
      "   --- Basic: %s should return [1, 7] for sum = 8" % l1)

print(sum_pairs(l2, -6) == [0, -6],
      "   --- Negatives: %s should return [0, -6] for sum = -6" % l2)

print(sum_pairs(l3, -7) == None,
      "   --- No Match: %s should return None for sum = -7" % l3)

print(sum_pairs(l4, 2) == [1, 1],
      "   --- First Match From Left: %s should return [1, 1] for\
      sum = 2 " % l4)

print(sum_pairs(l6, 8) == [4, 4],
      "   --- Duplicates: %s should return [4, 4] for sum = 8" % l6)

print(sum_pairs(l7, 0) == [0, 0],
      "   --- Zeroes: %s should return [0, 0] for sum = 0" % l7)

print(sum_pairs(l8, 10) == [13, -3],
      "   --- Subtraction: %s should return [13, -3] for sum = 10" % l8)

print(sum_pairs(l5, 10) == [3, 7],
      "   --- First Match From Left REDUX!: %s should return [3, 7]\
      for sum = 10 " % l5)
