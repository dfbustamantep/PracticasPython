from flask import Flask,request,make_response,redirect,render_template,session,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
import unittest

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"]='CLAVE SEGURA'

items ={"Arroz","Huevos","Cafe"}

class LoginForm(FlaskForm):
    username = StringField("Nombre del usuario",validators=[DataRequired()])
    password = PasswordField("Contrasenia",validators=[DataRequired()])
    submit = SubmitField("Enviar datos",validators=[DataRequired()])

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
    #response.set_cookie("user_ip_information",user_ip_information)
    session["user_ip_information"] = user_ip_information
    return response
    #return f"Hola,Como estas? tu direccion IP es la siguiente {user_ip_information}"
    #return 'Hello World!'

@app.route('/show_information_address',methods=["GET","POST"])
def show_information():
    user_ip =session.get('user_ip_information')
    username =session.get("username")
    login_form = LoginForm()
    context = {
        "user_ip":user_ip,
        "items":items,
        "login_form":login_form,
        "username":username
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"]=username
        flash("Nombre de usuario registrado correctamente")
        return redirect(url_for("index"))
    #return f"Hola que tal,tu direccion ip es {user_ip}"
                            #Busca en el carpeta templeates el archivo,la vairable de la izquierda es el valor que se esta llamando en el html
    return render_template('ip_information.html',**context)

if __name__ == "__main__":
    #desde cualquier direccion
    app.run(host='0.0.0.0',port=81,debug=True)  