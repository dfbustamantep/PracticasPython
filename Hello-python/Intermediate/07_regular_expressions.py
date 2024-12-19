## Expresiones regulares

import re

# match Busca solo al inicio de la primera linea de un string

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección",my_string,re.I)
print(match)
#span = match.span()
start,end = match.span()
#print(span) # Rango Tupla de dos valores
print(my_string[start:end])

match = re.match("Esta no es la lección",my_other_string)
# if not match==None 
# if match != None
if  match is not None:
    print(match)
    start,end = match.span()
    print(my_other_string[start:end])

print(re.match("Expressiones Regulares",my_string))

# search retorna el objeto sin importar en que parte del string este
search = re.search("lección",my_string,re.I)
print(search)
start,end = search.span()
print(my_string[start:end])


# findall Retorna una lista con todas las coincidencias

findall = re.findall("lección",my_string,re.I)
print(findall)

# split  toma un string y con la condicion que le demos retorna una lista

print(re.split(":",my_string))

# sub Reemplza las coincidencias con lo que le indiquemos

#print(re.sub("lección|Lección","LECCION",my_string))
print(re.sub("[l|L]ección","LECCION",my_string))
print(re.sub("Expresiones Regulares","RegEx",my_string))


'''
[]: A set of characters
[a-c] means, a or b or c
[a-z] means, any letter from a to z
[A-Z] means, any character from A to Z
[0-3] means, 0 or 1 or 2 or 3
[0-9] means any number from 0 to 9
[A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
\: uses to escape special characters
\d means: match where the string contains digits (numbers from 0-9)
\D means: match where the string does not contain digits
. : any character except new line character(\n)
^: starts with
r'^substring' eg r'^love', a sentence that starts with a word love
r'[^abc] means not a, not b, not c.
$: ends with
r'substring$' eg r'love$', sentence that ends with a word love
*: zero or more times
r'[a]*' means a optional or it can occur many times.
+: one or more times
r'[a]+' means at least once (or more)
?: zero or one time
r'[a]?' means zero times or once
{3}: Exactly 3 characters
{3,}: At least 3 characters
{3,8}: 3 to 8 characters
|: Either or
r'apple|banana' means either apple or a banana
(): Capture and group
https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md
'''

## Patterns
# Debemos poner la r antes
pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern,my_string))

pattern = r'[a-z]'
print(re.findall(pattern,my_string))
print(re.match(pattern,my_string))

pattern = r'[0-9]'
print(re.findall(pattern,my_string))
print(re.match(pattern,my_string))
print(re.search(pattern,my_string))

# solo numeros
pattern=r'\d'
print(re.findall(pattern,my_string))

# excluye numeros
pattern=r'\D'
print(re.findall(pattern,my_string))

pattern=r'[l].'
print(re.findall(pattern,my_string))

pattern=r'[l].*'
print(re.findall(pattern,my_string))

# Para aprender y validar expresiones regulares: https://regex101.com