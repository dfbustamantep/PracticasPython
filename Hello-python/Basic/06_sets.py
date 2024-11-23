# Sets
# 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente un diccionario

my_other_set ={"Daniel","Bustamante",20}
print(type(my_other_set)) # Ahora es un set por la forma de introducir datos

print(len(my_other_set))

my_other_set.add("DBustamante")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("DBustamante")
print(my_other_set)  # Un set no admite repetidos

print("Daniel" in my_other_set) # Miramos si el elemento esta dentro del set
print("DAniel" in my_other_set)

my_other_set.remove("Daniel") # Eliminamos el elemento
print(my_other_set)

my_other_set.clear() # Borra todos los elementos
print(my_other_set)

del my_other_set 


my_set ={"Daniel","Bustamante",20}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set={"C++","Java","Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_set).union({"JavaScript","C#"}))

print(my_new_set.difference(my_set))