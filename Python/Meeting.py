# https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python

# def meeting(s):
#     s = dict(i.split(":") for i in s.upper().split(";"))
#     s = sorted(s.items(), key=lambda x: x[0])
#     ss = {}
#     for i in s:
#         k, v = i[1], i[0]
#         ss[k] = v
#     ss = sorted(ss.items(), key=lambda x: x[0])
#     names = ""
#     for i in ss:
#         names += "(" + str(i[0]) + ", " + str(i[1]) + ")"
#     return names

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
