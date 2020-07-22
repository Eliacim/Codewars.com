# https://www.codewars.com/kata/588422ba4e8efb583d00007d/train/python

def late_ride(n):
    hour, minute = divmod(n, 60)
    result = sum(int(i) for i in str(hour)) + sum(int(i) for i in str(minute))
    return result


print(late_ride(240))  # 4)
print(late_ride(808))  # 14)
print(late_ride(50))  # 5
