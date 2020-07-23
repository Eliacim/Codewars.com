# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python


def format_duration(sec):
    seconds = sec % 60
    minutes = (sec // 60) % 60
    hours = (sec // 3600) % 24
    days = (sec // 86400) % 365
    years = (sec // 31104000)
    s = lambda x: "s" if x > 1 else ""
    return ''.join((f'{years} year{s(years)}, ' if years > 0 else "")
                   + (f'{days} day{s(days)}, ' if days > 0 else "")
                   + (f'{hours} hour{s(hours)}, ' if hours > 0 else "")
                   + (f'{minutes} minute{s(minutes)} and ' if minutes > 0 else "")
                   + (f'{seconds} second{s(seconds)}' if seconds > 0 else "" ))



print(format_duration(1))  # "1 second"
print(format_duration(62))  # "1 minute and 2 seconds"
print(format_duration(120))  # "2 minutes"
print(format_duration(3600))  # "1 hour"
print(format_duration(3662))  # "1 hour, 1 minute and 2 seconds" 3662
print(format_duration(3662*1000))  # "1 hour, 1 minute and 2 seconds"
print(format_duration(3600*24*366*366))  # "372 years, 1 day, 0 hour, 0 minute and 0 second"







'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
'''