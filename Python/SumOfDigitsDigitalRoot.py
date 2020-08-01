# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    return ((n - 1) % 9) + 1 if n else 0


print(digital_root(16))  # 7)
print(digital_root(942))  # 6)
print(digital_root(132189))  # 6)
print(digital_root(493193))  # 2)
