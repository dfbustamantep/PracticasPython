import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
bcrypt = Bcrypt()
# Utilidad que permite usar decoradores para proteger rutas
login_manager = LoginManager()
# Especificamos que vista se encarga de hacer el login
login_manager.login_view = 'authication.login_in_user'
# PErmite definir que tan fuerte va a ser la protección 
login_manager.session_protection="strong"

def creata_app(config_type):
    app = Flask(__name__)
    # Obtener la ruta actual y encontrar la carpeta config donde buscaremos un archivo
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    from app.auth import authentication
    app.register_blueprint(authentication)
    return app