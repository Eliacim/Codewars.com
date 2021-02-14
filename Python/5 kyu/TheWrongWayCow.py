"""

5 kyu
The Wrong-Way Cow

https://www.codewars.com/kata/57d7536d950d8474f6000a06

Have you ever noticed that cows in a field are always facing in the same
direction?

Reference: http://bfy.tw/7fgf

Well.... not quite always.

One stubborn cow wants to be different from the rest of the herd - it's that
damn Wrong-Way Cow!

Task
Given a field of cows find which one is the Wrong-Way Cow and return her
position.

Notes:

There are always at least 3 cows in a herd
There is only 1 Wrong-Way Cow!
Fields are rectangular
The cow position is zero-based [x,y] of her head (i.e. the letter c)



Examples

Ex1
cow.cow.cow.cow.cow
cow.cow.cow.cow.cow
cow.woc.cow.cow.cow
cow.cow.cow.cow.cow
Answer: [6,2]

Ex2
c..........
o...c......
w...o.c....
....w.o....
......w.cow
Answer: [8,4]


Notes

The test cases will NOT test any situations where there are "imaginary" cows,
so your solution does not need to worry about such things!

To explain - Yes, I recognise that there are certain configurations where an
"imaginary" cow may appear that in fact is just made of three other "real"
cows. In the following field you can see there are 4 real cows (3 are facing
south and 1 is facing north). There are also 2 imaginary cows (facing east and
west).

But such a field will never be tested by this Kata.

...w...
..cow..
.woco..
.ow.c..
.c.....

"""


def find_wrong_way_cow(field):
    left, right, up, down = [], [], [], []
    for r, row in enumerate(field):
        for c, col in enumerate(row):
            if row[c:c + 3] == ["c", "o", "w"]:
                left.append([c, r])
            elif row[c:c + 3] == ["w", "o", "c"]:
                right.append([c + 2, r])
            elif len(field) >= r + 2 and (row[c] == "c"
                                          and field[r + 1][c] == "o"
                                          and field[r + 2][c] == "w"):
                up.append([c, r])
            elif len(field) >= r + 2 and (row[c] == "w"
                                          and field[r + 1][c] == "o"
                                          and field[r + 2][c] == "c"):
                down.append([c, r + 2])
    return min([d for d in [left, right, up, down] if len(d) > 0], key=len)[0]


# This is the test part - already given by the KATA
# Function usable to show the field in the console:
def show(field):
    print('\n'.join(''.join(line) for line in field))
    return [line[:] for line in field]


field = list(map(list, ["cow.cow.cow.cow.cow",
                        "cow.cow.cow.cow.cow",
                        "cow.woc.cow.cow.cow",
                        "cow.cow.cow.cow.cow"]))

assert find_wrong_way_cow(show(field)) == [6, 2]

field = list(map(list, ["c..........",
                        "o...c......",
                        "w...o.c....",
                        "....w.o....",
                        "......w.cow"]))

assert find_wrong_way_cow(show(field)) == [8, 4]

field = list(map(list, ["cowc",
                        "cowo",
                        "coww",
                        "cow."]))

assert find_wrong_way_cow(show(field)) == [3, 0]
