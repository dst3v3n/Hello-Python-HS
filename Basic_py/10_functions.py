### Functions ###

def my_function ():
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()

def sum_two_values (firs_values: int , second_values: int):
    print(firs_values + second_values)

sum_two_values (5 , 7)
sum_two_values (54754 , 71231)
sum_two_values ("5" , "7")
sum_two_values (1.4 , 5.2)

def sum_two_values_with_return (firs_values , second_values):
    my_sum = firs_values + second_values
    return my_sum

my_result = sum_two_values (1.4 , 5.2)
print(my_result)

my_result = sum_two_values_with_return(10 , 5)
print(sum_two_values_with_return(10 , 5))

def print_name (name , surname):
    print(f"{name} {surname}")

print_name (surname="Sabogal" , name="Harold")

def print_name_with_default (name , surname , alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Harold" , "Sabogal")
print_name_with_default("Harold" , "Sabogal" , "MonekyDSabogal")

def print_upper_texts (*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts ("Hola", "Python" , "MonkeyDSabogal")
print_upper_texts ("Hola")