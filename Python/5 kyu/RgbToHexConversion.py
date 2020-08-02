'''
https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

5 kyu RGB To Hex Conversion

The rgb function is incomplete. Complete it so that passing in RGB decimal
values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255. Any values that fall out of that
range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3
will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''


def rgb(r, g, b):
    r = r if r >= 0 and r <= 255 else 0 if r < 0 else 255
    g = g if g >= 0 and g <= 255 else 0 if g < 0 else 255
    b = b if b >= 0 and b <= 255 else 0 if b < 0 else 255
    return "{:02x}{:02x}{:02x}".format(r, g, b).upper()


def rgb2(r, g, b):
    def numcheck(n):
        return max(0, min(n, 255))

    return ("{:02x}" * 3).format(numcheck(r), numcheck(g), numcheck(b)).upper()


print(rgb(0, 0, 0))  # "000000", "testing zero values")
print(rgb(1, 2, 3))  # "010203", "testing near zero values")
print(rgb(255, 255, 255))  # "FFFFFF", "testing max values")
print(rgb2(254, 253, 252))  # "FEFDFC", "testing near max values")
print(rgb2(-20, 275, 125))  # "00FF7D", "testing out of range values")
