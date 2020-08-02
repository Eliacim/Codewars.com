'''
https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python

6 kyu Meeting

John has invited some friends. His list is:

s =
"Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

Could you make a program that

makes this string uppercase gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first
name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL,
BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

It can happen that in two distinct families with the same family name two
people have the same first name too.

Notes You can see another examples in the "Sample tests".
'''


def meeting2(s):
    s = dict(i.split(":") for i in s.upper().split(";"))
    s = sorted(s.items(), key=lambda x: x[0])
    ss = {}
    for i in s:
        k, v = i[1], i[0]
        ss[k] = v
    ss = sorted(ss.items(), key=lambda x: x[0])
    names = ""
    for i in ss:
        names += "(" + str(i[0]) + ", " + str(i[1]) + ")"
    return names


def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':')))
                   for x in s.upper().split(';')))


print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;"
              + "Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;"
              + "Lewis:Kern;Megan:Stan;Alex:Korn"))
# (ARNO, ANN)(BELL, JOHN)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)
# (SCHWARZ, VICTORIA)(STAN, MEGAN)(WAHL, ALEXIS)

print(meeting("Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:Dorries;Ann:Kern;"
              + "Haley:Arno;Paul:Dorny;Madison:Kern"))
# (ARNO, ALEX)(ARNO, HALEY)(BELL, SARAH)(CORNWELL, ALISSA)(DORNY, PAUL)
# (DORRIES, ANDREW)(KERN, ANN)(KERN, MADISON)
