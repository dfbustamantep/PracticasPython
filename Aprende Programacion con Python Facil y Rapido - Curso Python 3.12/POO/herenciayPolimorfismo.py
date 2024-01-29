class Vehiculo:
    def __init__(self,marca,modelo) :
        self.marca = marca
        self.modelo = modelo
    
    def arrancar (self):
        return f"{self.marca} {self.modelo} esta arrancando"

#Herencia
class Coche(Vehiculo) :
    def acelear(self):
        return f"{self.marca} {self.modelo} esta acelerando"
    
class Motocicleta(Vehiculo) :
    def caballito(self):
        return f"{self.marca} {self.modelo} esta haciendo caballito"
    
cochee = Coche("Renault",2024)
print(cochee.arrancar())
print(cochee.acelear())

moto = Motocicleta("Kawazaki",2014)
print(moto.arrancar())
print(moto.caballito())