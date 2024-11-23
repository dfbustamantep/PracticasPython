# Tuplas

#Conjunto de valores

my_tuple = tuple()
my_other_tuple = (35,60,30)

my_tuple = (20,1.71 ,"Daniel","Bustamante")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Daniel"))
print(my_tuple.index("Daniel"))

# Las tuplas no se pueden modificar
# Inmutables
# my_tuple[1] = 1.80
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(tuple(my_tuple))

my_tuple[3] = "DBustamante"
my_tuple.insert(1,"Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminamos la tupla
del my_tuple
# print(my_tuple)
