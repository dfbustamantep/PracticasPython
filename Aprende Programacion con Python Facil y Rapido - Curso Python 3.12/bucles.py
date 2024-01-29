'''
#bucle WHILE mientras
i = 0
while i<10:
    i = i+1
    print("El numero es ",i)
'''
#Bucle infinito
'''while True:
    print(1)
'''

#Bucle for
'''
lista = {"hamburguesa","perro","pan","salchichas"}

for i in lista:
    print(i)

for numero in range(0,10):
    print(numero)
'''
print("Bucle for")
frutas = ["manzana","banana","cereza","naranja"]
contador = 0

#Bucle for itera sobre la lista de frutas
for fruta in frutas:
    contador += 1
    print(f"Fruta # {contador}: {fruta}")

numero = [1,2,3,4,5]
cuadrado = 0
for numeros in numero:
    cuadrado = numeros**2
    print(f"El cuadrado de {numeros} es: {cuadrado}")

#Bucle While
print("\nBucle while")
contador = 1
while contador <= 5:
    print(contador)
    contador +=1

print("\n")
contador = 10
while contador >= 1:
    print(f" {contador}! ")
    contador -=1
print("Feliz año")

print("\n")

suma=0
numero=0

numero=int(input("Ingrese un numero entero positivo (O un numero negativo para salir): "))

while numero >= 0:
    
    suma+=numero
    numero=int(input("Ingrese un numero entero positivo (O un numero negativo para salir): "))

print(f"La suma de los numeros ingresados es: {suma}")

