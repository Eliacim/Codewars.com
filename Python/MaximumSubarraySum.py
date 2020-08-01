# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

def max_sequence2(arr):
    low = maxresult = total = 0
    for i in arr:
        total += i
        low = min(low, total)
        maxresult = max(maxresult, total - low)
    return maxresult


def max_sequence(arr):
    max, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0:
            curr = 0
        if curr > max:
            max = curr
    return max


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
