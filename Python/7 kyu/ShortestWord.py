'''
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

7 kyu Shortest Word

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data
types.
'''


def find_short(s):
    return len(min(s.split(), key=len))


print(find_short("bitcoin take over the world maybe who knows perhaps"))  # 3)
print(find_short("turns out random test cases are easier "
                 + "than writing out basic ones"))  # 3)
print(find_short("lets talk about javascript the best language"))  # 3)
print(find_short("i want to travel the world writing code one day"))  # 1)
print(find_short("Lets all go on holiday somewhere very cold"))  # 2)
