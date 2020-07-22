# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


print(descending_order(0))  # 0
print(descending_order(15))  # 51
print(descending_order(123456789))  # 987654321
