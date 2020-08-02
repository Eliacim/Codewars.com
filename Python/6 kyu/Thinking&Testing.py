'''
https://www.codewars.com/kata/5a90c9ecb171012b47000077/train/python

6 kyu
Thinking & Testing: A * B?

'''


def test_it(a, b):
    aa = bb = 0
    for i in str(a):
        aa += int(i)
    for i in str(b):
        bb += int(i)
    return aa * bb


print(test_it(0, 1))  # 0)
print(test_it(1, 2))  # 2)
print(test_it(5, 6))  # 30)
print(test_it(10, 10))  # 1)
print(test_it(200, 200))  # 4)
print(test_it(12, 34))  # 21)
print(test_it(123, 45))  # 54)
