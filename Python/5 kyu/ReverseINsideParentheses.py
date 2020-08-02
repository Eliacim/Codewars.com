'''
https://www.codewars.com/kata/5e07b5c55654a900230f0229/train/python

5 kyu RGB To Hex Conversion

The rgb function is incomplete. Complete it so that passing in RGB decimal
values will result in a hexadecimal representation being returned. Valid
decimal values for RGB are 0 - 255. Any values that fall out of that range must
be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will
not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''


#
# I need to study this code founded in the internet
# I was so tired to make this kata - :(   shame on me!
#


def reverse_in_parentheses(string):
    output_stack = [""]
    stack_index = 0
    for ch in string:
        if ch == "(":
            stack_index += 1
            output_stack.append("")
        elif ch == ")":
            current_string = output_stack.pop()
            stack_index -= 1
            built_string = "(" + current_string + ")"
            if stack_index % 2 == 1:
                output_stack[stack_index] = built_string \
                                            + output_stack[stack_index]
            else:
                output_stack[stack_index] += built_string
        else:
            if stack_index % 2 == 1:
                output_stack[stack_index] = ch + output_stack[stack_index]
            else:
                output_stack[stack_index] += ch
    return output_stack.pop()


print(reverse_in_parentheses("h(el)lo"))
# "h(le)lo")

print(reverse_in_parentheses("a ((d e) c b)"))
# "a (b c (d e))")

print(reverse_in_parentheses("one (two (three) four)"))
# "one (ruof (three) owt)")

print(reverse_in_parentheses("one (ruof ((rht)ee) owt)"))
# "one (two ((thr)ee) four)")
