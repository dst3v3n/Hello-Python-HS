### Higher Order Functions ###

from functools import reduce

def sum_one (values):
    return values + 1

def sum_five (values):
    return values + 5

def sum_two_values_and_add_values (first_values:int , second_values:int , f_sum):
    return f_sum(first_values + second_values)

print (sum_two_values_and_add_values(5 , 2 , sum_one))
print (sum_two_values_and_add_values(5 , 2 , sum_five))

### Closures ###

def sum_ten (original_values):
    def add (values):
        return values + 10 + original_values
    return add

add_closure = sum_ten (1)
print (add_closure(5))
print((sum_ten(5))(1))

### Built-in Higher Order Functions ###

numbers = [2 , 5 , 10 , 21 , 3 , 30]

# Map

def multiply_two (number):
    return number * 2
print(list(map(multiply_two , numbers)))
print(list(map(lambda number: number * 2 , numbers)))  

# Recorre todos los valores y ejecuta sobre ello para modificar su valor 

# Filter 

def filter_greatter_than_ten (number):
    if number > 10:
        return True
    else:
        return False

print(list(filter(filter_greatter_than_ten , numbers)))
print(list(filter(lambda number: number > 10 , numbers)))

# Recorre todos los valores y ejecuta una funcion que retorna True o False para saber como filtrar los valores iterando

# Reduce

def sum_two_values (first_values , second_values):
    # print(first_values)
    # print(second_values)
    return first_values + second_values 

print (reduce (sum_two_values ,  numbers))

# Operar un valor mas el acomulado