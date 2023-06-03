### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [18 , 24 , 35 , 65 , 35 , 45, 80]

print(my_list)
print(len(my_list))

my_other_list = [18 , 1.79 , "Harold" , "Sabogal"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])

print(my_other_list.index("Harold"))

print(my_list.count(35)) #Cuenta las veces que esta ese dato

age, height, name, surname = my_other_list #Desempaquetar los datos de la lista. Lo numero de variables debe ser igual al len de la lista
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list) #Concatenar dos listas

my_other_list.append("Human Talent")
print(my_other_list)

my_other_list.insert(1, "black")
print(my_other_list)

my_other_list[1] = "Azul and Rojo"
print(my_other_list)

my_other_list.remove("Azul and Rojo")
print(my_other_list)

my_list.remove(35)
print(my_list)

print(my_list.pop()) #Sin ningun argumento,va a eliminar el ultimo valor
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element) 
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)
print(my_list)

my_list.clear() #Borrar el contenido de la lista
print(my_list)
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[0:2])

my_list = "Hola Python"
print(my_list)
print(len(my_list)) #Class str