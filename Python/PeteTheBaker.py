# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
    return min(available[x] // y for x, y in recipe.items()) \
        if all(True if item in available.keys() else False
               for item in recipe.keys()) else 0


def cakes2(recipe, available):
    return min(available.get(k, 0) / recipe[k] for k in recipe)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(recipe, available))  # 2

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}

print(cakes(recipe, available))  # 0
