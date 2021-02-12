"""
5 kyu ISBN-10 Validation

https://www.codewars.com/kata/51fc12de24a9d8cb0e000001

ISBN-10 identifiers are ten digits long. The first nine characters are digits
0-9. The last digit can be 0-9 or X, to indicate a value of 10.

An ISBN-10 number is valid if the sum of the digits multiplied by their
position modulo 11 equals zero.

For example:

ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
This is a valid
ISBN, because:

(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

Examples
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false

"""


def valid_ISBN102(isbn):
    if len(isbn) == 10 and isbn[:9].isdigit() and (
       isbn[9].isdigit() or isbn[9].lower() == "x"):
        validation = 0
        for e, i in enumerate(isbn.lower()):
            if i != "x":
                validation += (e + 1) * int(i)
            else:
                validation += (e + 1) * 10
        if (validation % 11) == 0:
            return True
    return False


def valid_ISBN10(isbn):
    if (len(isbn) == 10 and isbn[:9].isdigit() and (isbn[9].isdigit() or
                                                    isbn[9].lower() == "x")):
        validation = 0
        for e, i in enumerate(isbn.lower()):
            validation += (e + 1) * (int(i) if i != "x" else 10)
        return True if validation % 11 == 0 else False
    return False


assert valid_ISBN10('1112223339')
assert valid_ISBN10('048665088X')
assert valid_ISBN10('1293000000')
assert valid_ISBN10('1234554321')
assert not valid_ISBN10('1234512345')
assert not valid_ISBN10('1293')
assert not valid_ISBN10('X123456788')
assert not valid_ISBN10('ABCDEFGHIJ')
assert not valid_ISBN10('XXXXXXXXXX')