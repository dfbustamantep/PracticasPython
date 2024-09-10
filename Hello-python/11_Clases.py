# Clases 

class MyEmptyPerson:
    # Para dejar vacio algo,funciones o clases
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    # Contructor ,self es siempre neccesario
    def __init__(self,name,surname,alias = "Sin alias"):
        # self.name = name
        # self.surname = surname
        # Publico
        self.full_name = f"{name} {surname}"
        # Privados
        self.__name = name
        self.__surname = surname
        self.__alias = name

    def get_name(self):
        return self.__name
    
    def walk (self):
        print(f"{self.full_name} Esta caminando")
    
my_person = Person("Daniel","Bustamante","DBustamante")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Daniel","Bustamante")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (El loco de los perros)"
print(my_other_person.full_name)