'''
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python

6 kyu Who likes it?

You probably know the "like" system from Facebook and other pages. People can
"like" blog posts, pictures or other items. We want to create the text that
should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input
array, containing the names of people who like an item. It must return the
display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others
like this"

'''


def likes(names):
    res = ""
    if not names:
        res = "no one likes this"
    elif len(names) == 1:
        res = names[0] + " likes this"
    elif len(names) < 3:
        res = names[0] + " and " + names[1] + " like this"
    elif len(names) < 4:
        res = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif len(names) > 3:
        res = names[0] + ", " + names[1] + " and " + str(len(names) - 2) \
              + (" others like this" if len(names) > 3 else " other like this")
    return res


print(likes([]))  # 'no one likes this')
print(likes(['Peter']))  # 'Peter likes this')
print(likes(['Jacob', 'Alex']))  # 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']))  # 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
# 'Alex, Jacob and 2 others like this')
