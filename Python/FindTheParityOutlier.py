# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
    even = [i for i in integers if i % 2 == 0]
    odd = [i for i in integers if i % 2 == 1]
    return even[0] if len(even) < len(odd) else odd[0]


print(find_outlier([2, 4, 6, 8, 10, 3]))  # 3)
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))  # 11)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))  # 160)
