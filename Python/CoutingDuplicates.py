# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    return len([t for t in set(text.lower()) if text.lower().count(t) > 1])


print(duplicate_count("abcde"))  # 0
print(duplicate_count("abcdea"))  # 1
print(duplicate_count("indivisibility"))  # 1
