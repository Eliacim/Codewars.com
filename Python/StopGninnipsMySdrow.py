# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python


def spin_words(sentence):
    return ' '.join(s[::-1] if len(s) > 4 else s for s in sentence.split())


print(spin_words("Welcome"))  # emocleW
print(spin_words("Hey fellow warriors"))  # Hey wollef sroirraw
