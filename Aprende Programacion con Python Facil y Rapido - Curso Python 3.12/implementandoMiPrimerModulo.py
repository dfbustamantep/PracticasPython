import miPrimerModulo

numero1 =int (input("Digite un numero "))
numero2 =int (input("Digite un numero "))

suma =miPrimerModulo.suma(numero1,numero2)
resta =miPrimerModulo.resta(numero1,numero2)
multiplicacion =miPrimerModulo.multiplicacion(numero1,numero2)
division =miPrimerModulo.division(numero1,numero2)

print(f"El resultado de las operaciones basicas con los numeros {numero1} y {numero2} es:")
print(f"\nSuma:{suma}")
print(f"Resta:{resta}")
print(f"Multiplicacion:{multiplicacion}")
print(f"Division:{division}")