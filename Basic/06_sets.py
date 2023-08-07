### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un dict

my_other_set = {"Harold", "Sabogal", 18}
print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set[0])  # No se puede acceder a los elementos

my_other_set.add("MonekyDSabogal") # Un set no es una estructura ordenada
print(my_other_set) 

my_other_set.add("MonekyDSabogal") # Un set no admite elementos repetidos
print(my_other_set)

print("Harold" in my_other_set)
print("Ha" in my_other_set)

my_other_set.remove("Harold")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set)

my_set = {"Harold", "Sabogal", 18}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Python", "JavaScript", "Java"}

my_new_set =  my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Docker", "PHP", "DataBases"}))

print(my_new_set.difference(my_set))