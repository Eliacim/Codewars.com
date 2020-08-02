'''
https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

6 kyu Build Tower

Build Tower Build Tower by the following given argument: number of floors
(integer and always greater than 0).

Tower block is represented as *

Python: return a list; JavaScript: returns an Array; C#: returns a string[];
PHP: returns an array; C++: returns a vector<string>; Haskell: returns a
[String]; Ruby: returns an Array; Lua: returns a Table; Have fun!
'''


def tower_builder2(n_floors):
    i = 1
    temp = ""
    tower = []
    while i <= n_floors:
        if i == 1:
            temp = " " * (n_floors - i) + "*" * i + " " * (n_floors - i)
        else:
            temp = " " * (n_floors - i) + "*" * (i + (i - 1)) + " " * \
                (n_floors - i)
        tower.append(temp)
        i += 1
    return tower


def tower_builder(n):
    return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]


print(tower_builder(1))  # *
print(tower_builder(2))  # *, ***
print(tower_builder(3))  # *, ***, *****
print(tower_builder(4))  # *, ***, *****, *******

#
#    *    1       3
#   ***   2+1     2
#  *****  3+2     1
# *******  4+3    0
