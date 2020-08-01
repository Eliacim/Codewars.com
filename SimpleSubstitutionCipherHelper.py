'''
https://www.codewars.com/kata/52eb114b2d55f0e69800078d

6 kyu Simple Substitution Cipher Helper

A simple substitution cipher replaces one character from an alphabet with a
character from an alternate alphabet, where each character's position in an
alphabet is mapped to the alternate alphabet for encoding or decoding.

E.g.

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"

If a character provided is not in the opposing alphabet, simply leave it as be.
'''

# This is my code:
class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2

    def encode(self, s):
        return ''.join([self.map2[self.map1.find(ss)] if ss in self.map1
                       else ss for ss in s])

    def decode(self, s):
        return ''.join([self.map1[self.map2.find(ss)] if ss in self.map2
                        else ss for ss in s])


# This is one of the best voted code in codewars:
class Cipher2(object):
    def __init__(self, map1, map2):
        self.encode_map = dict(zip(map1, map2))
        self.decode_map = dict(zip(map2, map1))

    def encode(self, string):
        return ''.join(self.encode_map.get(c, c) for c in string)

    def decode(self, string):
        return ''.join(self.decode_map.get(c, c) for c in string)


# Test phase:
map1 = "abcdefghijklmnopqrstuvwxyz"
map2 = "etaoinshrdlucmfwypvbgkjqxz"

cipher = Cipher(map1, map2)
print(cipher.encode("ab&c"))  # , "eta");
print(cipher.encode("xyz"))  # , "qxz");
print(cipher.decode("eirfg"))  # , "aeiou");
print(cipher.decode("erlang"))  # , "aikcfu");
print('----------------------')

map2 = 'tfozcivbsjhengarudlkpwqxmy'
cipher = Cipher(map1, map2)
print(cipher.encode('abc'))  # , 'tfo');
print(cipher.decode('tfo'))  # , 'abc');
print(cipher.decode('kjpphi'))  # , 'tjuukf');
print(cipher.encode('ajqqtb'))  # , 'tjuukf');
