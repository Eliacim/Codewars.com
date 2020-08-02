'''
https://www.codewars.com/kata/5625618b1fe21ab49f00001f

8 kyu Grasshopper - Debug sayHello

Debugging sayHello function The starship Enterprise has run into some problem
when creating a program to greet everyone as they come aboard. It is your job
to fix the code and get the program working again!

Example output:

Hello, Mr. Spock
'''


def say_hello(name):
    return "Hello, " + name if name else name


print(say_hello('Mr. Spock'))  # 'Hello, Mr. Spock')
print(say_hello('Captain Kirk'))  # 'Hello, Captain Kirk')
print(say_hello('Liutenant Uhura'))  # 'Hello, Liutenant Uhura')
print(say_hello('Dr. McCoy'))  # 'Hello, Dr. McCoy')
print(say_hello('Mr. Scott'))  # 'Hello, Mr. Scott')
