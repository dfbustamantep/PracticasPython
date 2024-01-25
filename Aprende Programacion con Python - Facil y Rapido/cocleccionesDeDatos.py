'''
#listas
deportes = ["futbol","basquet","tenis"]

print(deportes)

print(deportes[0])

#asignamos el valor de rugby al primer campo de nuestra lista
deportes[0]="volleyball"

print(deportes)
print(deportes[0])

#imprimimos el tamaño de nuestra lista
print(len(deportes))

#agregamos un elemento a la lista
deportes.append("rugby")
print(deportes)

#agregar en un lugar especifico de la lista
deportes.insert(0,"rugby")
print(deportes)

#eliminar un elemento especifico de la lista
deportes.remove("tenis")
print(deportes)

#eliminar un elemento especifico de la lista por posicion
deportes.pop(0)
print(deportes)

#limpiar la lista
deportes.clear()
print(deportes)

deportes1 = ["bolos","natacion"]

#agregar los valores de una lista a otra
deportes.extend(deportes1)
print(deportes)

numeros =[2,3,6,1,8,0]
print(numeros)

numeros.sort()
print(numeros)

'''

#tuplas,parecidos a las listas pero no se puede modificar los valores 
numeros = (1,2,3,4,5,6)
print(numeros)

#posicion en la que esta un valor
print(numeros.index(1))

#veces en la que esta un valor
print(numeros.count(1))

#diccionarios 
#Los diccionarios tienen llave y valor
misDatos = {
    "nombre":"Daniel",
    "edad":19,
    "pais":"Colombia"

}

print(type(misDatos))

print(misDatos)
#acceder a un dato en especifico
print(misDatos["nombre"])

#cambiar un valor espefcifico
misDatos["nombre"] = "Felipe"
print(misDatos["nombre"])


#acceder a las llaves
print(misDatos.keys())
#acceder a los valores
print(misDatos.values())