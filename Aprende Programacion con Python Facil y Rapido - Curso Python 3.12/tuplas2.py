personas=(("juan",25),("maria",16),("carlos",20))

#como la tupla tiene dos datos creamos dos variables
for nombre,edad in personas:
    if edad>18:
        print(f"{nombre} tiene {edad},cumple con la mayoria de edad")


numeros = (10,20,30,40,50)
suma = sum(numeros)
print(f"La suma de los numeros es {suma}")