#Las listas pueden ser modificadas,alteradas o reestructuradas

#Lista de enteros
numeros = [1,2,3,4,5]

#Lista de cadenas de texto
frutas =["manzana","banana","cereza"]

#Listas mixtas
mixta = [1,"hola",3.14,True]

#mostrar una lista en pantalla
print(numeros)
print(frutas)
print(mixta)

#mostrar un dato especifico de la lista por su posicion
print(numeros[0])
print(frutas[1])
print(mixta[3])

#modificar un elemento en la lista
numeros[2] = 9
print(numeros)

#agregar un dato
numeros.append(8)
print(numeros)

frutas.append("coco")
print(frutas)

#eliminar elementos dentro de la lista
del numeros[2]
print(numeros)

del frutas[0]
print(frutas)

for fruta in frutas:
    print(fruta)

suma = sum(numeros)
print(suma)