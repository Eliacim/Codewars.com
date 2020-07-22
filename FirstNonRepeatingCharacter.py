# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

def first_non_repeating_letter(string):
    return ''.join([s for s in string if string.lower().count(s.lower())
                    == 1][:1])


print(first_non_repeating_letter('a'))  # 'a')
print(first_non_repeating_letter('stress'))  # 't')
print(first_non_repeating_letter('moonmen'))  # 'e')
print(first_non_repeating_letter(''))  # '')
print(first_non_repeating_letter('abba'))  # '')
print(first_non_repeating_letter('aa'))  # '')
print(first_non_repeating_letter('~><#~><'))  # '#')
print(first_non_repeating_letter('hello world, eh?'))  # 'w')
print(first_non_repeating_letter('sTreSS'))  # 'T')
print(first_non_repeating_letter('Go hang a salami, I\'m a \
                                 lasagna hog!'))  # ','
