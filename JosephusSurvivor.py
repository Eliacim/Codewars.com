# https://www.codewars.com/kata/555624b601231dc7a400017a/train/python

def josephus_survivor(n, k):
    circle = list(range(1, n + 1))
    i = 0
    while len(circle) > 1:
        i = (i + k - 1) % len(circle)
        circle.pop(i)
    return circle[0]


print(josephus_survivor(7, 3))  # 4)
print(josephus_survivor(11, 19))  # 10)
print(josephus_survivor(1, 300))  # 1)
print(josephus_survivor(14, 2))  # 13)
print(josephus_survivor(100, 1))  # 100)
