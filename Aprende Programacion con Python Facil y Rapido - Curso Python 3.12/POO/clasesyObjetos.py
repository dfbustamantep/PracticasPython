class Persona:
    #constructor
    def __init__(self,nombre,edad) :
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola,mi nombre es {self.nombre} y tengo {self.edad}")

#Crear una instancia de la clase persona
persona1 = Persona("juan",18)

#Llamar al metodo saludar
persona1.saludar()

#Crear una instancia de la clase persona
persona2 = Persona("Maria",20)

#Llamar al metodo saludar
persona2.saludar()