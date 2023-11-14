""" 
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */ 
 """

def invertir (texto:str):
    invertir = texto[::-1]  #toma todos los caracteres de la cadena texto, pero en orden inverso.
    return invertir