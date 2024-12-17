## Error types


# SyntaxError
#print "Hola comunidad" # DEwscomentar para error
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print ("Hola comunidad")

# NameError
language = "Spanish" # Comentar para error
print(language)
# NameError: name 'language' is not defined

# IndexError
my_list =["Python","C#","Java","C++"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[-1])
# print(my_list[5]) # Descomentar para ver error

# ModuleNotFound
#import maths # Descomentar para ver el error
import math

# AttributeError
#print(math.PI)
print(math.pi)

# KeyError
my_dict ={"Nombre":"Daniel","Apellido":"Bustamante","Edad":20,1:"Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"])# Descomentar para ver el error
print(my_dict["Apellido"])

# TypeError
# print(my_list["Nombre"])# Descomentar para ver el error
print(my_list[0])

# ImportError
# from math import PI # Descomentar para ver el error
from math import pi
print(pi)

# ValueError
my_int = int("10")
#my_int = int("10 años") # Descomentar para ver el error
print(type(my_int))

# ZeroDivisonError
print(5/2)
#print(5/0) # Descomentar para ver el error