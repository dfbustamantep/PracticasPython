# Condicionales

my_condition = True
if my_condition:
    print("Se ejecuta la condicion del if")
    
my_condition = 1

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if") 

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20") 
    
elif my_condition == 25:
    print("Es igual a 1")
    
else:
    print("Es menor o igual que 10 o igual que 20 o distinto a 25")

print("La ejecucion continua")

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacia")