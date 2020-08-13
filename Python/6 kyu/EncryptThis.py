'''
https://www.codewars.com/kata/5848565e273af816fb000449

6 kyu Encrypt this!

Acknowledgments: I thank yvonne-liu for the idea and for the example tests :)

Description: Encrypt this!

You want to create secret messages which can be deciphered by the Decipher
this! kata. Here are the conditions:

Your message is a string containing space separated words. You need to encrypt
each word in the message using the following rules: The first letter needs to
be converted to its ASCII code. The second letter needs to be switched with the
last letter Keepin' it simple: There are no special characters in input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''


def encrypt_this(string):
    string = string.split()
    res = []
    for ss in string:
        if len(ss) == 3:
            ss = ss[:1] + ss[2] + ss[1]
        elif len(ss) > 3:
            ss = ss[:1] + ss[-1] + ss[2:-1] + ss[1]
        else:
            ss = ss
        ss = ss.replace(ss[0], str(ord(ss[0])), 1)
        res.append(ss)
    return ' '.join(r for r in res)


print(encrypt_this(""))  # "")
print(encrypt_this("A wise old owl lived in an oak"))
# "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
print(encrypt_this("The more he saw the less he spoke"))
# "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
print(encrypt_this("The less he spoke the more he heard"))
# "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
print(encrypt_this("Why can we not all be like that wise old bird"))
# "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
print(encrypt_this("Thank you Piotr for all your help"))
# "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
