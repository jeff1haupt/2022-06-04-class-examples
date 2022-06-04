var_a = 10 # global scope

def sum_of_three_numbers():
    var_b = 5
    var_c = 5
    # var_a = 5 # local scope takes precedent 
    # var_a = var_a + 10

    print(var_a + var_b + var_c)

sum_of_three_numbers()
print(var_a)
# print(var_b)
