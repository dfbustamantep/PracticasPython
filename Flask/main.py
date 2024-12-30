from flask import Flask,request,make_response,redirect,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

items ={"Arroz","Huevos","Cafe"}


@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html',error=error)

# endpoint punto final o ruta
@app.route('/index')
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    response.set_cookie("user_ip_information",user_ip_information)
    return response
    #return f"Hola,Como estas? tu direccion IP es la siguiente {user_ip_information}"
    #return 'Hello World!'

@app.route('/show_information_address')
def show_information():
    user_ip =request.cookies.get('user_ip_information')
    context = {
        "user_ip":user_ip,
        "items":items
    }
    #return f"Hola que tal,tu direccion ip es {user_ip}"
                            #Busca en el carpeta templeates el archivo,la vairable de la izquierda es el valor que se esta llamando en el html
    return render_template('ip_information.html',**context)
#desde cualquier direccion
app.run(host='0.0.0.0',port=81,debug=True)