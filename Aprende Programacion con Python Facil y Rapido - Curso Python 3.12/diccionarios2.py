#diccionario anidado
personas={
    "persona1":{
        "nombre":"Juan",
        "edad":19,
        "ciudad":"Madrid"
    },
    "persona2":{
        "nombre":"Maria",
        "edad":28,
        "ciudad":"Barcelona"
    },
    "persona3":{
        "nombre":"Carlos",
        "edad":35,
        "ciudad":"Valencia"
    }
}

datos = personas["persona1"]
datos2 = personas["persona2"]
datos3 = personas["persona3"]


print(datos["nombre"])
print(datos2["nombre"])
print(datos3["nombre"])

persona1= {
    "nombre":None,
    "edad":None,
    "direccion":None,
    "telefono":None
}

persona1["nombre"]=input("Digite su nombre: ")
persona1["edad"]=int(input("Digite su edad: "))
persona1["direccion"]=input("Digite su direccion: ")
persona1["telefono"]=(input("Digite su telefono: "))

print(persona1["nombre"],"tiene ",persona1["edad"],"años, vive en",persona1["direccion"],"y su numero de telefono es",persona1["telefono"])