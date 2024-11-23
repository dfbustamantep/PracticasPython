from fastapi import APIRouter

# Es prfefix lo que ahce es que en los parametros de las funciones no haya necesidad de poner /products,el tag sirve para en la documentacion se vea aparte con un titulo de products
router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404:{"message":"No encontrado"}})

products_list = ["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5"]

@router.get("/")
async def products():
    return ["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5"]

@router.get("/{id}")
async def products(id:int):
    return products_list[id]