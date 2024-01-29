'''
class Auto:
    color = "Rojo"
    puertas = 4

    #Self se refier al objeto o instancia de clase,,permitiendo acceder a los atibutos y metodos de la instancia
    def avanzar(self):
        print("Arrancando coche")

miCoche = Auto()
print(miCoche.color)
print(miCoche.puertas)

miCoche.avanzar()
'''

class Auto:
    def __init__(self,puertas,color,marca,gasolina):
        self.puertas = puertas
        self.color = color
        self.marca = marca
        self.gasolina = gasolina

    def avanzar(self):
        if self.gasolina > 0:
            print("Andando")
        else:
            print("No hay gasolina")

    def conducir(self):
        for litro in range (0,self.gasolina):
            if litro >0 :
                self.gasolina -= 1
                print(f"Quedan {self.gasolina} litros")

            else:
                print("Sin gasolina")

porsche = Auto(2,"Amarillo","Porshe",80)

print(porsche.puertas)
print(porsche.avanzar())
print(porsche.conducir())
            


            