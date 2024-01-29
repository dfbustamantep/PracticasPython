#Encapsulamiento
class Encap:
    def __init__(self):
        #self.__numero = 0 hace que el atributo sea privado
        
        self.numero = 0

    def operacion(self):
        print(self.numero+20)

    def resultado(self):
        return self.numero
    
ejemplo = Encap()
ejemplo.operacion()
ejemplo.numero=100
print(ejemplo.resultado())