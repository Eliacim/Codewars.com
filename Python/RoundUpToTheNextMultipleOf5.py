# https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/python

def round_to_next5_2(n):
    if n % 5 == 0:
        n = n
    else:
        n = (n // 5) * 5 + 5
    return n


def round_to_next5(n):
    return n if n % 5 == 0 else (n // 5) * 5 + 5


print(round_to_next5(0))
print(round_to_next5(2))
print(round_to_next5(5))
print(round_to_next5(12))
print(round_to_next5(30))
print(round_to_next5(-2))
