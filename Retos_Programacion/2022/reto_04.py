""" 
/* ÁREA DE UN POLÍGONO
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */ 
"""

class Poligono:
    def __init__(self):
        self.__base = None
        self.__altura = None
        self.__lado1 = None
        self.__lado2 = None

    def Triangulo (self , Base:int or float , Altura: int or float):
        self.__base = Base
        self.__altura = Altura
        return (Base*Altura)/2
    
    def Cuadrado (self, Lado1: int or float , Lado2: int or float):
        self.__lado1 = Lado1
        self.__lado2 = Lado2
        return Lado1*Lado2
    
    def Rectangulo (self, Base:int or float , Altura: int or float):
        self.__base = Base
        self.__altura = Altura
        return Base*Altura