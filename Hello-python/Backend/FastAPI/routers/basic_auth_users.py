from fastapi import FastAPI,Depends, HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordBearer,OAuth2PasswordRequestForm

app = FastAPI()
# estandar que nos dice como trabajar cn autenticacion
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
# Para levantar el servidor: uvicorn basic_auth_users:app --reload

class User(BaseModel):
    username:str
    full_name:str
    email:str
    disabled:int

class UserDB(User):
    password:str

users_db = {
    "mouredev":{
        "username":"mouredev",
        "full_name":"Brais Moure",
        "email":"braismoure@mouredev.com",
        "disabled":False,
        "password":"123456"
    },
    "mouredev2":{
        "username":"mouredev2",
        "full_name":"Brais Moure 2",
        "email":"braismoure2@mouredev.com",
        "disabled":True,
        "password":"654321"
    },
}
def search_user_db(username:str):
    if username in users_db:
        # usamos los ** para decir que pueden haber varios parametros
        return UserDB(**users_db[username])
    
def search_user(username:str):
    if username in users_db:
        # usamos los ** para decir que pueden haber varios parametros
        return User(**users_db[username])

async def current_user(token:str =Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales de autenticacion invalidas",
                            headers={"WWW-Authenticate":"Beare"})
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Usuario inactivo",
                            )
    return user

@app.post("/login")
# Depends va a recibir datos pero no depende de nadie
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username )
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="El usuario no es correcto")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="La constraseña no es correcta")
    
    return {"acces_token":user.username,"token_type":"bearer"}

@app.get("/users/me")
async def me(user:User = Depends(current_user)):
    return user