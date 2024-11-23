#String

my_string = 'Mi String'
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string+" "+my_other_string)

my_new_line_string = 'Esto es un String\ncon salto de linea'
print(my_new_line_string)

my_new_tab_string = 'Esto es un String\tcon tabulacion'
print(my_new_tab_string)

# Formateo
name,surname,age = 'Daniel' , 'Bustamante',20


print("Mi nombre es Daniel Bustamante")

print("Mi nombre es {} {}  y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s  y mi edad es %s" %(name,surname,age))
print(f"Mi nombre es {name} {surname}  y mi edad es {age}")


# Desempaquetado de caractares
language = "Python"
a,b,c,d,e,f= language
print(a)
print(e)

# Division
language_slice = language [1:3]
print(language_slice)

language_slice = language [1:]
print(language_slice)

language_slice = language [-2]
print(language_slice)

# Reverse
reversed_language = language [::-1]
print(reversed_language)

# Funciones
# Pone la priemra letra en mayuscula
print(language.capitalize())

print(language.upper())

print(language.count("t"))

print(language.isnumeric())

print("1".isnumeric())

print(language.lower())
