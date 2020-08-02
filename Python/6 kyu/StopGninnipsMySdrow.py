'''
https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

6 kyu Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and returns the
same string, but with all five or more letter words reversed (Just like the
name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test" spinWords( "This is
another test" )=> returns "This is rehtona test"
'''


def spin_words(sentence):
    return ' '.join(s[::-1] if len(s) > 4 else s for s in sentence.split())


print(spin_words("Welcome"))  # emocleW
print(spin_words("Hey fellow warriors"))  # Hey wollef sroirraw
