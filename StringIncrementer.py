# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

def increment_string(strng):
    word = strng.rstrip('1234567890')
    num = strng[len(word):]
    return word + (str(1 + int(num)).zfill(len(num))) \
        if len(num) != 0 else strng + '1'


print(increment_string("foo"))  # "foo1")
print(increment_string("foobar001"))  # "foobar002")
print(increment_string("foobar1"))  # "foobar2")
print(increment_string("foobar00"))  # "foobar01")
print(increment_string("foobar99"))  # "foobar100")
print(increment_string("foobar099"))  # "foobar100")
print(increment_string(""))  # "1")
