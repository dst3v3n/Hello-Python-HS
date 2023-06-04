### Exceptions Handling ###

numberOne = 5 
numberTwo = 1
numberTwo = "1"

# try except

try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except:
    # Esto se produce si hay una excepción
    print("Se ha producido un error")

# Try except else finally

# numberOne = 5 
# numberTwo = 1

try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: #Opcional
    # Se ejecuta si no se ejecuta una excepción 
    print("La ejecucion continua correctamente")
finally: #Opcional
    # Se ejecuta siempre
    print("La ejecucion continua")

# Excepciones por tipo

try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la informacion de la expeción

try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except TypeError as error: #Capturar el error
    print(error)


try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except ValueError as error: #Capturar el error
    print(error)
except Exception as exception:
    print(exception)