# Manejo de  Excepciones

numberOne = 5 
numberTwo = "1"

# print(numberOne+numberTwo)

# try Except
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")


# try Except else
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se genera una excpecion
    print("La ejecucion continua correctamente")
    
# try Except else finally
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se genera una excpecion
    print("La ejecucion continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecucion continua")
    
# Captura de excepciones por tipo
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")
    
# Captura de la informacion de la excepcion
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except ValueError as VE:
    print("Se ha producido un ValueError ",VE)
except TypeError as TE:
    print("Se ha producido un TypeError ",TE)
#Cualquier excepcion    
except Exception as exception:
    print(exception)