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
- Se deben definir rutas o endpoints para nuestra aplicacion
```bash
    @app.route('/home')
    def hello():
        return 'Hello World!'
```
- Ponemos en funcionamiento el servidor de flask
```bash
    app.run(host='0.0.0.0',port=81)
```
- Si queremos hacer debuggin debemos poner un parametro mas
```bash
    app.run(host='0.0.0.0',port=81,debug=True)
```
- Objeto request
    - Nos permite obtener todos los datos que vienen del cliente
```bash
    from flask import request
```
- Objeto response
    - Nos permite obtener todos los datos que vienen del cliente
```bash
    from flask import make_response,redirect
```
    - Nos permite redireccionar