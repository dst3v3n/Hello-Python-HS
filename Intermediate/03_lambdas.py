### Lambdas ###

sum_two_values = lambda firs_values, second_values: firs_values + second_values 
print(sum_two_values(2 , 4))

multiply_values = lambda firs_values, second_values: firs_values * second_values - 3
print (multiply_values( 2 , 4))

def sum_three_values (values):
    return lambda firs_values , second_values: firs_values + second_values + values

print (sum_three_values (5)(2,4))