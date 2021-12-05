'''
5 kyu
Don't Drink the Water

Don't Drink the Water

Given a two-dimensional array representation of a glass of mixed liquids, sort
the array such that the liquids appear in the glass based on their density.
(Lower density floats to the top) The width of the glass will not change from
top to bottom.

    ======================
|   Density Chart    |
======================
| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |
----------------------

[                            [
 ['H', 'H', 'W', 'O'],        ['O',  'O',  'O',  'O']
 ['W', 'W', 'O', 'W'],  =>    ['W',  'W',  'W',  'W']
 ['H', 'H', 'O', 'O']         ['H',  'H',  'H',  'H']
 ]                           ]

The glass representation may be larger or smaller. If a liquid doesn't fill a
row, it floats to the top and to the left.

'''


from functools import reduce


def separate_liquids(glass):
    if not glass:
        return glass

    items = reduce(lambda x, y: x + y, glass)
    items.sort(key=lambda x: "OAWH".index(x))
    size = len(glass[0])

    glass = [items[i:i + size] for i in range(0, len(items), size)]

    return glass


assert separate_liquids([['A', 'H', 'W', 'A']]) == [['A', 'A', 'W', 'H']]

print("Should be able to sort 3 liquids")

assert separate_liquids([['H', 'H', 'W', 'O'], ['W', 'W', 'O', 'W'],
                         ['H', 'H', 'O', 'O']]) == \
                         [['O', 'O', 'O', 'O'], ['W', 'W', 'W', 'W'],
                          ['H', 'H', 'H', 'H']]

print("Should be able to handle 4 liquids")
assert separate_liquids([['A', 'A', 'O', 'H'], ['A', 'H', 'W', 'O'],
                         ['W', 'W', 'A', 'W'], ['H', 'H', 'O', 'O']]) == \
                        [['O', 'O', 'O', 'O'], ['A', 'A', 'A', 'A'],
                         ['W', 'W', 'W', 'W'], ['H', 'H', 'H', 'H']]

print("Should be able to handle one row")
assert separate_liquids([['A', 'H', 'W', 'O']]) == [['O', 'A', 'W', 'H']]

print("Should be able to handle one column")
assert separate_liquids([['A'], ['H'], ['W'], ['O']]) == \
                        [['O'], ['A'], ['W'], ['H']]

print("Should be able to handle empty array")
assert separate_liquids([]) == []
