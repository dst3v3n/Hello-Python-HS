""" 
/* LA SUCESIÓN DE FIBONACCI
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */ 
"""

def fibonacci (rang:int):
    before = 0
    after = 1
    for i in range (rang + 1):
        fibo = before + after
        before = after
        after = fibo
        print(fibo)
    
fibonacci(150)
