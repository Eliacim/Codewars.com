# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk2(walk):
    ew = ns = 0
    for w in walk:
        if w == 'n':
            ns += 1
        if w == 's':
            ns -= 1
        if w == 'e':
            ew += 1
        if w == 'w':
            ew -= 1
    return True if (ew == 0 and ns == 0 and len(walk) == 10) else False


def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and \
        walk.count('e') == walk.count('w')


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # T
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w',
                     'e', 'w', 'e', 'w', 'e']))  # F
print(is_valid_walk2(['w']))  # False
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # F
print(is_valid_walk(['e', 'w', 'e', 'w', 'n', 's', 'e', 's', 'e', 'w']))  # F
print(is_valid_walk2(['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']))  # T
print(is_valid_walk(['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 'e']))  # F
print(is_valid_walk2(['s', 'w', 'n', 'n', 'n', 'e', 's', 's']))  # False
