# Ciclos

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
#Python toma el bucle while similar a un condicional por lo que podemos poner un else
else:
    print("Mi condicion es mayor o igual que 10")  
    
print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        print("Se detiente la ejecucion")
        break
    print(my_condition)
    
print("La ejecucion continua")

# For
my_list = [35,24,62,52,30,30,17]

for element in my_list:
    print(element)
    
my_tuple = (20,1.71,"Daniel","Bustamante","DBustamante") 

for element in my_tuple:
    print(element)

my_set = {"Daniel","Bustamante",20}

for element in my_set:
    print(element)

my_dict ={"Nombre":"Daniel","Apellido":"Bustamante","Edad":20}

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
else:
    print("El bucle for para el diccionario ha finalizado")
    
print("La ejecucion continua")