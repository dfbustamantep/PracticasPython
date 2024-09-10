# Funciones

# funcion simple
def my_function():
    print("Esto es una funcion")
    
my_function()

# funcion con parametros
def sum_two_values(first_value:int,second_value:int):
    print(first_value+second_value)

sum_two_values(5,7)
sum_two_values(58899,7254)
# sum_two_values("5","7")
sum_two_values(1.4,5.2)

# funcion con retorno
def sum_two_values_with_return(first_value:int,second_value:int):
    my_sum = first_value+second_value
    return my_sum
    
my_result = sum_two_values_with_return(10,5)
print(my_result)

def print_name (name,surname):
    print(f"{name} {surname}")
    
print_name(surname = "Bustamante",name = "Daniel")

# Damos un valor por defecto
def print_name_with_default(name,surname,alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Daniel","Bustamante")
print_name_with_default("Daniel","Bustamante","DBustamante")

# El asterisco me indica que de ese tipo de dato le puedo pasr la cantidad que quiera
def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
    
print_upper_texts("Hola","Ejemplo","Adios")
print_upper_texts("Hola")
