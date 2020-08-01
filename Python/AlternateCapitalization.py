# https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python

def capitalize(s):
    s1 = s2 = ""
    s11 = []
    i = 0
    while i < len(s):
        if i % 2 == 0:
            s1 += s[i].upper()
            s2 += s[i].lower()
        else:
            s1 += s[i].lower()
            s2 += s[i].upper()
        i += 1
    s11.append(s1)
    s11.append(s2)
    return s11


def capitalize2(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]


print(capitalize("abcdef"))
print(capitalize2("abracadabra"))
