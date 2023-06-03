### Tuples ###

#Una tuple no es mutable

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (18, 1.79, "Harold", "Sabogal", "Harold")
my_other_tuple = (30, 30, 45, 40, 80)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Harold"))
print(my_tuple.count("10"))
print(my_tuple.index("Sabogal"))
print(my_tuple.index("Harold"))

# my_tuple[1] = 1.90 TypeError
# print(my_tuple) 

my_sum_tuple  = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3 : 6])  #Rebanadas

my_tuple = list( my_tuple )
print(type(my_tuple))

my_tuple[4] = "Human Talent"
my_tuple.insert(1, "rojo")
print(my_tuple)

print(tuple(my_tuple))
print(type(my_tuple))

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
print(my_tuple) #NameError