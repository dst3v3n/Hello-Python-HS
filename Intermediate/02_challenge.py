### Challenges ###


""" Reto #0: EL FAMOSO "FIZZ BUZZ”
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""

def fizzbuzz ():
    for i in range (1 , 101):
        if i % 3 == 0:
            print (f"{i} fizz")
        elif i % 5 == 0:
            print (f"{i} buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print (f"{i} fizzbuzz")
        else:
            print(i)
fizzbuzz()


""" 
/* Reto #1: ¿ES UN ANAGRAMA?
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def is_anamagrama (string1:str , string2:str):
    if string1.lower() == string2.lower():
        return False
    return sorted(string1.lower()) == sorted(string2.lower())

print(is_anamagrama("amor" , "roma"))



"""  Reto #2: LA SUCESIÓN DE FIBONACCI
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */ 
"""

def fibonaccion (rango:int):
    prev = 0
    next = 1
    for i in range (rango):
        print (prev)
        fibo = prev + next
        prev = next
        next = fibo

fibonaccion (50)


""" 
/* Reto #3: ¿ES UN NÚMERO PRIMO?
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */ 
"""
def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)


is_prime()