# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    return '{:02}:{:02}:{:02}'.format(seconds // 3600, seconds // 60 % 60,
                                      seconds % 60)


print(make_readable(0))  # "00:00:00")
print(make_readable(5))  # "00:00:05")
print(make_readable(60))  # "00:01:00")
print(make_readable(86399))  # "23:59:59")
print(make_readable(359999))  # "99:59:59")
