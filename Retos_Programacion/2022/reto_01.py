""" 
/* ¿ES UN ANAGRAMA?
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def anagrama (first_value:str , second_value:str):
    if first_value.lower() == second_value.lower():
        return False
    return sorted(first_value.lower()) == sorted(second_value.lower())