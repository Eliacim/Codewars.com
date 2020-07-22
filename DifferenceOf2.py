def twos_difference(lst):
    lst = sorted(lst)
    lst2 = []
    for l in lst:
        if (l + 2) in lst:
            lst2 += [(l, l + 2)]
    return lst2


print(twos_difference([1, 3, 4, 6]))
