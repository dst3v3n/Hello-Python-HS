"""
 /* Reto #8: DECIMAL A BINARIO
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */ 
 """

def binarios (numero:int):
    binario = []
    division = numero
    while division > 0:
        binarios = division % 2
        division //= 2
        binario.append(binarios)
    for i in range(10):
        if not(len(binario) % 4 == 0):
            binario.append(0)
    return binario[::-1]

print(binarios (1)) 
# binarios (127)