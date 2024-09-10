# Listas

# Estructura de datos - listas
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [20,24,30,35,24,52,30]

print(my_list)
print(len(my_list))

my_other_list = [20,1.70,"Daniel","Bustamante"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[-3])

# Retorna el numero de veces que aparece un elemento
print(my_list.count("Daniel"))
print(my_list.count(30))

# Concatenamos las listas
print(my_list + my_other_list)

# Insertamos al final
my_other_list.append("DBustamanteP")
print(my_other_list)

#Insertamos en la posicion que queremos
my_other_list.insert(1,"Azul")
print(my_other_list)


#Eliminar un valor
my_other_list.remove("Azul")
print(my_other_list)

#Elimina el elemento quew le ponemos como parametro
my_list.remove(30)
print(my_list)

# Quitamos el ultimo elemento y lo retorna
print(my_list.pop())
print(my_list)

# Podemos pasarle el indice del elemento que estamos desapilando
print(my_list.pop(2))
print(my_list)

# Eliminamos el elemento por indice
del my_list[2]
print(my_list) 


# Agregamos el elemento en el indice 1
my_other_list.insert(1,"Rojo")
print(my_other_list)

# Modificamos el elemento del indice 1
my_other_list[1] = "Azul"
print(my_other_list)

# Copiamos los elementos de my_list
my_new_list = my_list.copy()

# Borramos/limpiamos toda la lista
my_list.clear()
print(my_list)
print(my_new_list)

# ORganizamos al reves
my_new_list.reverse()
print(my_new_list)

# Organiza de menor a mayor,tambien podemos pasarle un parametro para organizar    
my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])

# Le cambiamos el tipo de dato a my_list pasamos de una lista a un str
my_list = "Hola Python"
print(my_list)
print(type(my_list))

