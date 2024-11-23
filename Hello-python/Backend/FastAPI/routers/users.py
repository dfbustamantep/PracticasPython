from fastapi import APIRouter,HTTPException
# Par definir una entidad
from pydantic import BaseModel
router = APIRouter( tags=["users"])

# Para levantar el servidor: uvicorn users:app --reload

# entidad user - le BaseModel permite crear y trbajar con una entidad
class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int
    
users_list=[User(id=1,name="Daniel",surname="Bustamante",url="https://github.com/dfbustamantep",age=20),
       User(id=2,name="Bustamante",surname="Daniel",url="https://github.com/dfbustamantep",age=20),
       User(id=3,name="Felipe",surname="Bustamante Perez",url="https://github.com/dfbustamantep",age=20)
       ]

@router.get("/usersjson")
async def usersjson():
    return [{"name":"Daniel","surname":"Bustamante","URL":"https://github.com/dfbustamantep","age":20},
            {"name":"Bustamante","surname":"Daniel","URL":"https://github.com/dfbustamantep","age":20},
            {"name":"Felipe","surname":"Perez","URL":"https://github.com/dfbustamantep","age":20}]
    
@router.get("/users")
async def users():    
    return users_list

# PATH pasar un parametro de la url
@router.get("/user/{id}")
async def user(id:int):  
    # Funcion de orden superior porque hace operaciones complicadas
    return serch_user(id)
    
# Pueden ir por la query queire decir que nosotros podemos indicarle casi lo que queamos
# http://127.0.0.1:8000/userquery/?id=3
@router.get("/userquery/")
async def user(id:int):  
    # Funcion de orden superior porque hace operaciones complicadas
    return serch_user(id)

# para devolver un codigo http usamos status code
# en caso correcto response model    
@router.post("/user/",response_model=User,status_code=201)    
async def user(user:User):
    if type(serch_user(user.id)) ==User:
        # Cuando lanzamos un error toca con raise
        raise HTTPException(status_code=404,detail="El usuario ya existe")
        #return {"error":"El usuario ya existe"}
    else:
        users_list.append(user)
        return user

@router.put("/user/")
async def user(user:User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user

@router.delete("/user/{id}")
async def user(id:int):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index] 
            found = True
            
    if not found:
        return {"error":"No se ha eliminado el usuario"}
            
    
def serch_user(id:int):
     # Funcion de orden superior porque hace operaciones complicadas
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}