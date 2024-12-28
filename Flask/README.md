## Flask
- Documentación
https://flask.palletsprojects.com/en/stable/

- Recomendado usar entornos virtuales (venv)
```bash
    py -3 -m venv .venv
```
- Activar el entorno
```bash
    .venv\Scripts\activate
```
- Instalar Flask y los paquetes que requiere 
```bash
    pip install flask
```
- Guardar todas las liubrerias que necesitamos
```bash
    pip freeze > requirements.txt
```
- Importar flask
```bash
    from flask import Flask
```
- Instanciar la clase,al decir __name__ hacemos referencia al nombre de nuestro archivo
```bash
    app = Flask(__name__)
```