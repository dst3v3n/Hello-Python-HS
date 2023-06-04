### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__ (self , name , surname , alis = "Sin alias"): #Constructor de clase
        self.full_name = f"{name} {surname} ({alis})" #Propiedad publica
        self.__name = name # Propiedad privada
    
    def get_name (self):
        return self.__name

    def walk (self):
        print(f"{self.full_name} Esta caminando")

my_person = Person ("Harold" , "Sabogal")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Harold" , "Sabogal" , "MonkeyDSabogal")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Hector de Leon (El loco por los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)