## Flask
### Documentación
[Documentacion Flask en Español](https://flask.palletsprojects.com/es/stable/)

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
    <li><b>Herencia de templates: </b>Crear un template base (HTML) y usar en otrs archivos sin reptir el código</li>
    <li><b>Macros:</b> Archivo HTML que contienene funciones dentro de JINJA que permite renderizar ciertas plantillas para determinadas partes de nuestra interfaz </li>
    <li><b>Objeto Session:</b>En python existe este objeto que nos permite guardar de forma encripatada cierto tipo de datos </li>
    <!--<li><b></b> </li>-->
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

- Herencia de templates,crear un archivo base.html en la carpeta de templates
```jinja
    {% extends 'base.html'%}

    {% block title %}
        {{ super() }}
            Welcome
    {% endblock %}
```

- Macros,crear un archivo macros.html en la carpeta de templates
```jinja
    {% macro render_items(item)%}
        <li>Detalles del producto: {{item}}</li>
    {% endmacro %}
```

```html
    <ul>
        {% for item in items%}
            {{macros.render_items(item)}}
        {% endfor %}
    </ul>
```
- Reutilizando templates estaticos,se usa cuando queremos usar un template completo
```html
    <nav>
        <ul>
            <li><a href="{{url_for('index')}}">Boton inicio</a></li>
            <li><a href="hhtps://ww.google.com"></a>Google</li>
        </ul>
    </nav>
```
```jinja
    <header>
        {%include 'navbar.html'%}
    </header>
```
- Manejar archivos estaticos en FLASK
    <p>Debemos crear una carpeta static en el directorio raiz,ejemplo usando el nav que creamos anteriormente y una imagen en una carpeta images en la carpeta static,en la carpeta static tambien manejamos nuestro CSS</p>

    ```html
    <nav>
        <ul>
            <img src="{{url_for('static',filename='images/flask_font.png')}}" alt="">
            <li><a href="{{url_for('index')}}">Boton inicio</a></li>
            <li><a href="hhtps://ww.google.com"></a>Google</li>
        </ul>
    </nav>
    ```

- Controlando errores en Flask
    <p>Cuando vamos a una ruta que no exite flask nos sdaca un error 404,usnado un decorador especial podemos manejar nuestros errores </p>

    ```python
    @app.errorhandler(404)
    def not_found_endpoint(error):
        return render_template('404.html',error=error)
    ```

    ```html
    {%extends 'base.html'%}
    {%block title%}
        {{super()}}
        404
    {%endblock%}

    {%block content%}
        <h2>El recurso no existe</h2>
        {{error}}
    {%endblock%}
    ```
- Flask bootstrap,la libreria de bootrsap viene con un base html con toda la estrucutra
```
    pip install flask-bootstrap 
```
```python
    from flask_bootstrap import Bootstrap
```
```python
    from flask import request,make_response,redirect,render_template

    from flask_bootstrap import Bootstrap

    app = Flask(__name__)
    bootrap = Bootstrap(app)  
```

```html
    {%extends 'bootstrap/base.html'%}
    {%block head%}
    {{super()}}

    <title>
        {% block title %} Flask Aplication Web| {% endblock %}
    </title>
    <link rel="stylesheet" href="{{url_for('static',filename='css/style.css')}}">
    {%endblock%}

    {%block body%}
        {%block navbar%}
            {%include 'navbar.html'%}
        {%endblock%}

        {% block content %}
        {% endblock %}
    {%endblock%}
```
```html
    <nav class="navbar navbar-default">
        <img src="{{url_for('static',filename='images/flask.jpg')}}" alt="">
        <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">Flask App</a>
        </div>
        <ul class="nav navbar-nav">
            <li class="active"><a href="{{url_for('index')}}">Boton inicio</a></li>
            <li><a href="https://www.google.com">Boton google</a></li>

        </ul>
        </div>
    </nav>
```
- Añadir configuraciones a FLASK
    <p>El entorno de configuracion de FLASK por defecto es producción</p>
    <p>Con el objeto session encirptamos los datos de la sesion y desencirpatmos con CLAVE SEGURA</p>

    ```python
        from flask import session;
        app.config["SECRET_KEY"]="CLAVE SEGURA"

        @app.route("/index")
        def index():
            user_ip=request.remote_addr
            response = make_response(redirect("/show_information_addres"))
            session["user_ip_information"] = user_ip_information
    return response

        @app.route('/show_information_address')
        def show_information():
            user_ip =session.get('user_ip_information')
            username =session.get("username")
            context = {
                "user_ip":user_ip,
                "items":items,
                "username":username
            }

            return render_template('ip_information.html',**context)
    ```
- Formularios con Flask wtf
```python
    pip install flask-wtf
```

```python
    from flask-wtf import FLaskForm
    from wtfoms.fields import StringField,PasswordField,SubmitField
    from wtfoms.fields import DataRequired
    # En esta clase se implementan los campos que va a tener nuestro formulario
    class LoginForm(FlaskForm):
        username = StringField("Nombre del usuario",validators=[DataRequired()])
        password = PasswordField("Contraseña",validators=[DataRequired()])
        submit = SubmitField("Enviar datos",validators=[DataRequired()])
```

```python
    @app.route('/show_information_address')
def show_information():
    user_ip =session.get('user_ip_information')
    username =session.get("username")
    login_form = LoginForm()
    context = {
        "user_ip":user_ip,
        "items":items,
        "login_form":login_form
    }
    return render_template('ip_information.html',**context)
```
```jinja
    {% import 'bootstrap/wtf.html' as wtf%}

    {{wtf.quick_form(login_form)}}

```

- Metodo POST en flask
    <p> Los endpoints de Flaks por defecto aceptan solicitudes de tipo get y necesitamos especificarle el resto de metodos https </p>

    ```python
    @app.route('/show_information_address',methods=["GET","POST"])
    def show_information():
        user_ip =session.get('user_ip_information')
        username =session.get("username")
        login_form = LoginForm()
        context = {
            "user_ip":user_ip,
            "items":items,
            "login_form":login_form
            "username":username
        }
        if login_form.valdate_on_submit():
            username=login_form.username.data
            session["username"]=username
            return make_response(redirect("/index"))
        return render_template('ip_information.html',**context)
    ```
- Mensajes Flash
    <p>Mensajes o alertas</p>

 ```python
    form flask import url_for,flash
    @app.route('/show_information_address',methods=["GET","POST"])
    def show_information():
        user_ip =session.get('user_ip_information')
        username =session.get("username")
        login_form = LoginForm()
        context = {
            "user_ip":user_ip,
            "items":items,
            "login_form":login_form
            "username":username
        }
        if login_form.valdate_on_submit():
            username=login_form.username.data
            session["username"]=username
            flash("Nombre de usuario registrado correctamente")
            return redirect(url_for("index"))
        return render_template('ip_information.html',**context)
 ```

 ```jinja
        {% for message in get_flashed_messages() %}
        <div class="alert alert-success alert-dismissible">
            <button type="button" data-dismiss="alert" class="close">
                &times;
            </button>
            {{message}}
        </div>
    {%endfor%}

    {%block scripts%}
        {{super()}}
    {%endblock%}
 ```

 - Blueprints
    <p>Forma para mdoularizar nuestra aplicacion</p>
</section>