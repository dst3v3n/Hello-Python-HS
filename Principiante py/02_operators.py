### operadores Aritmeticos###

print(3 + 4) #Suma
print(3 - 4) #Resta
print(3 * 4) #Multiplicacion
print(3 / 4) #Division
print(10 % 2) #Modulo
print(10 // 3) #Floor division
print(2 ** 3) #Exponenciacion
print(2 ** 3 + 3 - 7 / 1 // 4) 

print ("Hola" + "Python" + "¿Que tal?") 
print("Hola" + str(5))
print("Hola" * 5)
print("Hola" * (2 ** 3))
print("Hola" * int(2 ** 3 + 3 - 7 / 1 // 4))
print("Hola" * int(2.5 * 2))

my_float = 2.5*2
print("Hola" * int(my_float))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("aaaa" >= "AAAA")
print(len("aaaa") >= len("abaa")) #Cuenta caractereres
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" == "Hola") #Ordenacion alfabettica por ASCII
print("Hola" != "Python")

### Operadores logicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))