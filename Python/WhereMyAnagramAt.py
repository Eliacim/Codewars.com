# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

def anagrams2(word, words):
    result = []
    for w in words:
        if sorted(w) == sorted(word):
            result.append(w)
    return result


def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# ['aabb', 'bbaa'])

print(anagrams2('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
# ['carer', 'racer'])
