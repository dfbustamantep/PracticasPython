## Flask
### Documentación
[Documentacion Flask en Español](https://flask.palletsprojects.com/en/stable/)

<nav>

</nav>

<h2>Conceptos</h2>
<ul>
    <li><b>Flask:</b> Framework de desarrollo web que también nos sirve para crear API's</li>
    <li><b>JINJA:</b> Nos permite renderizar los templates (Motor de templates)</li>
    <li><b>Endpoint:</b> Ruta</li>
    <li><b>Request:</b> Solicitud que viene del cliente al servidor</li>
    <li><b>Response:</b> Respuesta que el servidor le envia al cliente despues de su solicitud</li>
    <li><b>Templates:</b> Nos sirve para renderizar archivos HTML dinamico o estatico</li>
    <li><b>url_for: </b>Funcion que permite crear un link hacia un url de flask donde solo decimos el nombre de la funcion  </li>
    <li><b></b> </li>
    <li><b></b> </li>
</ul>

<section>
<h2>Entornos virtuales</h2>

- Se recomienda le uso de entornos virtuales (venv) ,para evitar problemas con las dependencias 

```python
    py -3 -m venv .venv
```
- Activar el entorno
```python
    .venv\Scripts\activate
```
</section>

<section>
<h2>Instalación y uso de Flask</h2>

- Instalar Flask y los paquetes que requiere flask por defecto
```python
    pip install flask
```
- Guardar todas las libreréas que necesitamos en un txt 
```python
    pip freeze > requirements.txt
```

- Importar flask
```python
    from flask import Flask
```
- Instanciar la clase,al decir __name__ hace referencia al nombre del archivo en el que se esta
```python
    app = Flask(__name__)
```
- Se deben definir rutas o endpoints para nuestra aplicacion
```python
    @app.route('/home')
    def hello():
        return 'Hello World!'
```
- Se debe poner en funcionamiento el servidor de flask
```python
    app.run(host='0.0.0.0',port=81)
```
- Si se quiere hacer debugging se debe poner un parametro mas
```python
    app.run(host='0.0.0.0',port=81,debug=True)
```
- Objeto request
```python
    from flask import request
```
- Objeto response
```python
    from flask import make_response,redirect
```
- Templates
```html
    <h2>Hola que tal,tu direccion ip es {{user_ip}}</h2>
```
- Condiciones con JINJA
```jinja
    {% if user_ip %}
        <h2>Hola que tal,tu direccion ip es {{user_ip}}</h2>
    {% else %}
        <a href="{{ url_for('index') }}">Else</a>
    {% endif %}
```

- Ciclos con JINJA
```python
    items=["item1","item2","item3","item4"]
```
```jinja
    <ul>
        {% for item in items %}
            <li>{{item}}</li>
        {% endfor %}
    </ul>
```
</section>