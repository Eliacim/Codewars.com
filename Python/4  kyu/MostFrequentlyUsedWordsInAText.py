"""

4 kyu
Most frequently used words in a text

https://www.codewars.com/kata/51e056fe544cf36c410000fb



Write a function that, given a string of text (possibly with punctuation and
line-breaks), returns an array of the top-3 most occurring words, in descending
order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more
apostrophes (') in ASCII. (No need to handle fancy punctuation.) Matches should
be case-insensitive, and the words in the result should be lowercased. Ties may
be broken arbitrarily. If a text contains fewer than three unique words, then
either the top-2 or top-1 words should be returned, or an empty array if a text
contains no words.


Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to
call to mind, there lived not long since one of those gentlemen that keep a
lance in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most nights,
scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays,
made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]


Bonus points (not really, but just for fun): Avoid creating an array whose
memory footprint is roughly as big as the input text. Avoid sorting the entire
array of unique words.

"""


import re
from collections import Counter


# Working for static tests, but not for dynamic
def top_3_words3(text):
    new = {}
    result = []
    text = re.sub("[^\w\d'\s]+", "", text.lower()).strip()
    if re.findall("\w", text):
        for t in text.split():
            if t not in new:
                new[t] = text.split().count(t)
        for x, y in sorted(new.items(), key=lambda t: t[1])[::-1]:
            if len(result) < 3:
                result.append(x)
    return result


# Using Collections > Counter
def top_3_words2(text):
    txt = Counter(re.findall("'*[a-z][a-z']*", text.lower()))
    top = [k for k, v in txt.most_common(3)]
    return top


# Simplifying the last one
def top_3_words(text):
    return [word for word, count in Counter(
            re.findall("'*[a-z][a-z']*", text.lower())).most_common(3)]


assert top_3_words("a a a  b  c c  d d d d  e e e e e") == ["e", "d", "a"]

assert top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")\
    == ["e", "ddd", "aa"]

assert top_3_words("  //wont won't won't ") == ["won't", "wont"]

assert top_3_words("  , e   .. ") == ["e"]

assert top_3_words("  ...  ") == []

assert top_3_words("  '  ") == []

assert top_3_words("  '''  ") == []

assert top_3_words("""In a village of La Mancha, the name of which I have
no desire to call to mind, there lived not long since one of those gentlemen
that keep a lance in the lance-rack, an old buckler, a lean hack, and a
greyhound for coursing. An olla of rather more beef than mutton, a salad on
most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""")\
    == ["a", "of", "on"]