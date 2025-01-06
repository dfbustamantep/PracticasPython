from flask import request,make_response,redirect,render_template,session,url_for,flash
import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

items ={"Arroz","Huevos","Cafe"}


@app.cli.command()
def test():
    test = unittest.TestLoader().discover("tests")
    unittest.TextTestResult().run(test)


@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html',error=error)

# endpoint punto final o ruta
@app.route('/index')
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
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
                            #Busca en el carpeta templeates el archivo,la vairable de la izquierda es el valor que se esta llamando en el html
    return render_template('ip_information.html',**context)

if __name__ == "__main__":
    #desde cualquier direccion
    app.run(host='0.0.0.0',port=81,debug=True)  