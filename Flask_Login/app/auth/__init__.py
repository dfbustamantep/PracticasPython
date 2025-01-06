from flask import Blueprint
                            #nombre del blueprint
authentication = Blueprint('authication', __name__,template_folder="templates")

from app.auth import routes