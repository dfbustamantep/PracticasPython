nombre = "Daniel"
apellido = "Bustamante"
frase = "Hola,esta es una frase"

#Contar todos los caracteres
longitud = len(nombre)
print(longitud)

longitud = len(apellido)
print(longitud)

longitud = len(frase)
print(longitud)

#Miramos un solo caracter de la cadena,aca podemos modificar la cadena
print(nombre[0])

#Separar la cadena
palabras = frase.split()
print(palabras)

#Cadena en mayuscula
mayuscula = apellido.upper()
print(mayuscula)

#Cadena en minuscula
minuscula = apellido.lower()
print(minuscula)

#Reemplazar una palabra
mensaje = "Hola mundo"
#primer parametro palabra que se quiere cambiar,segunda palabra palabra por la que se cambia
cambio = mensaje.replace("Hola","Adios")
print(mensaje)
print(cambio)


for i in apellido:
    print(i)

