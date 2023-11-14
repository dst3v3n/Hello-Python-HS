""" 
/* Reto #7: CONTANDO PALABRAS
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */ 
 """

def countWord (text:str):
    suma = 0
    string = text.lower()
    new_string = []
    for i in string:
        new_string.append(i)
    for i in range (len(string)):
        for h in new_string:
            if not(h == " " or h == "," or h == "."):
                if  string[i] == h:
                    q = h
                    suma += 1
                    new_string.pop(new_string.index(q))
        if suma > 1:
            print(f"La palabra {q} esta repetida {suma} veces")
        elif suma == 1:
            print(f"La palabra {q} esta repetida {suma} vez")
        suma = 0

countWord ("Hola mundo, hola python")