from flask import Blueprint
                            #nombre del blueprint
authentication = Blueprint('authentication', __name__,template_folder="templates")

from app.auth import routes