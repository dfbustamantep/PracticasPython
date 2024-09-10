# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Clave valor
my_other_dict = {"Nombre":"Daniel","Apellido":"Bustamante","Edad":20,1:"Python"}
my_dict = {
    "Nombre":"Daniel",
    "Apellido":"Bustamante",
    "Edad":20,
    "Lenguajes":{"C++","Java","Python"},
    1:1.70
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
my_dict["Nombre"] = "Juan"

print(my_dict["Nombre"])

my_dict["Calle"] = "Cll 62"
print(my_dict)

# Eliminamos un solo elemento,el elemento calle
del my_dict["Calle"]
print(my_dict)

print("Daniel" in my_dict) # estamos buscando por clave
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("Nombre",1)))

my_list = ["Nombre",1,"Piso"]

my_new_dict = my_other_dict.fromkeys(("Nombre",1,"Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,["Daniel","Bustamante"])# Mete a todas las clases esos valores
print(my_new_dict)

my_valuies = my_new_dict.values()
print(type(my_valuies))

print(my_new_dict.values())
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))