# 4 things needed to define a function: 1) 'def' keyword 2) function name 3) parameter list - can be empty, and 4) a ':'
def simple_multiplication(x, y): #  <--- notice the 4 requirements???
    print(f"{x} / {y} = { x/y }")
    print(f'{x} x {y} = {x * y}') # this is a void function

# to 'call' the function you just need to type the name and any required parameters in paranthesis '()'
# number = simple_multiplication(10, 5)
# print(number)

def returned_value(x, y, z):
    return x + y + z

sum_of_values = returned_value(1, 2, 3) # because this is returning the sum we can assign it to a variable 
# print(sum_of_values)

simple_multiplication(returned_value(1, 2, 3), int(input("Enter a number: ")))