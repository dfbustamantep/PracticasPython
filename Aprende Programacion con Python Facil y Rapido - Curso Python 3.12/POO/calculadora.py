class calculadora:
    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2

    def multiplicacion(self, num1, num2):
        return num1 * num2
    
    def division(self,num1,num2):
        if num2 == 0:
            print("No se puede dividir por 0")
            return None
        return num1/num2
    
num1 = float(input("Digite un numero "))
num2 = float(input("Digite un numero "))

clc = calculadora()

resSum = clc.suma(num1, num2)
resRes = clc.resta(num1, num2)
resMul = clc.multiplicacion(num1, num2)
resDiv = clc.division(num1, num2)

print(f"El resultado de las operaciones con los numeros {num1} y {num2}")

print(f"Suma {resSum}")
print(f"Resta {resRes}")
print(f"Multiplicacion {resMul}")
print(f"Division {resDiv}")