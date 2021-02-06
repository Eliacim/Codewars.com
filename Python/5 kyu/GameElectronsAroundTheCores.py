"""

5 kyu
Game - Electrons around the cores

https://www.codewars.com/kata/52210226578afb73bd0000f1


Have you heard of the game "electrons around the cores"? I'm not allowed to
give you the complete rules of the game,   just so much:

the game is played with 4 to 6 dice, so you get an array of 4 to 6 numbers,
each 1-6
the name of the game is important
you have to return the correct number five times in a row and your solution is
considered to be correct
If you just press "submit", you'll get an array and the expected value!

Here are some input/output pairs for you to wrap your mind around:
 
[ 1, 2, 3, 4, 5 ] -> 6
[ 2, 2, 3, 3 ] -> 4
[ 6, 6, 4, 4, 1, 3 ] -> 2
[ 3, 5, 3, 5, 4, 2 ] -> 12
And yes, it is a shameless copy of a famous game.
"""


def electrons_around_the_cores2(dice):
    result = 0
    for d in dice:
        if d == 3:
            result += 2
        elif d == 5:
            result += 4
    return result


# I simplified the solution above
def electrons_around_the_cores(dice):
    return sum([2 if d == 3 else 4 if d == 5 else 0 for d in dice])


# This was the most voted version / clever:
def electrons_around_the_cores3(dice):
    return dice.count(3) * 2 + dice.count(5) * 4


rolling = [([1, 1, 1, 1], 0),
           ([2, 2, 2, 2], 0),
           ([1, 1, 1, 3], 2),
           ([1, 1, 3, 3], 4),
           ([1, 3, 3, 3], 6),
           ([3, 3, 3, 3], 8),
           ([4, 4, 4, 4], 0),
           ([1, 1, 1, 5], 4),
           ([1, 1, 5, 5], 8),
           ([1, 5, 5, 5], 12),
           ([5, 5, 5, 5], 16),
           ([6, 6, 6, 6], 0)]

for dice, result in rolling:
    assert electrons_around_the_cores(dice) == result
