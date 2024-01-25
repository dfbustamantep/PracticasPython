'''
numero = 10
numero1 = 20
numero2 = 30


if(numero == numero1):
    print("Los numeros son iguales")
elif(numero<numero1):
    print("El primer numero es el mayor")
elif(numero>numero1):
    print("El segundo numero es mayor")
else:
    print("Los numeros son diferentes")

#losdos deben ser menores
if numero and numero1 < numero2:
    print("Los numeros 1 y 2 son menores")
#uno de los dos debe ser menor
if numero or numero1 < numero2:
    print("Los numeros 1 y 2 son menores")

n1=10
n2=40

if not n1==n2:
    print("n1 y n2 no son iguales")
'''

edad =int(input("Digite su edad "))

if(edad<18):
    print("Es menor de edad")
elif(edad==18):
    print("Tiene 18 años")
else:
    print("Es mayor de edad")