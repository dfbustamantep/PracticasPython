'''def saludar(nombre):
    print(f"Hola {nombre}")

saludar("daniel")
'''
#------------------------
def suma(a,b):
    resultado = a + b
    return resultado

n1 =int(input("Digite un numero "))
n2 =int(input("Digite un numero "))
dato = suma(n1,n2)
print(f"El resultado de la suma de {n1} y {n2} es {dato}")

#-----------------------
def esPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    

numero = int(input("Digite un numero "))
if esPar(numero) == True :
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

#-------------------------------------
def listaNumeros (lista):
    maximo = max(lista)
    return maximo

numeros=[1,2,3,4,5,6,7,900,4,100]
valor = listaNumeros(numeros)
print(f"El mayor de los numeros de la lista es {valor}")