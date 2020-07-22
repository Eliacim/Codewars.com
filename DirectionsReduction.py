def dirReduc(arr):
    directions = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST",
                  "WEST": "EAST"}
    final = []
    for i in arr:
        if final and directions[i] == final[-1]:
            final.pop()
        else:
            final.append(i)
    return final


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
# ['WEST']
