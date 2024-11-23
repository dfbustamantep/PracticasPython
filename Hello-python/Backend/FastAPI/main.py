from fastapi import FastAPI
from routers import products,users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
# para montar
app.mount("/static",StaticFiles(directory="static"),name="static")

# Siempre que llamamos a un servidor la operacion que se ejecuta debe ser asincrona
@app.get("/")
async def root():
    return "Hola FastAPI!"

# http://127.0.0.1:8000     
# Para levantar el servidor: 
# main es el nombre del fichero y app es la instancia de fastAPI que creamos
# Detener el server: CTRL + C

@app.get("/url")
async def url():
    return {"url":"https://mouredev.com/python"}

# Documentacion con Swagger: /docs
# si ponemos /docs al ejecutar miraremos toda la documentacion del proyecto que estamos haciendo
# Documentacion con Redocly: /redoc
# si ponemos /redoc al ejecutar miraremos toda la documentacion del proyecto que estamos haciendo  

# GET obtener datos 
# POST para crear datos
# PUT para actualizar datos
# DELETE para borrar datos
