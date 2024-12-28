from flask import Flask

app = Flask(__name__)

# endpoint punto final o ruta
@app.route('/home')
def hello():
    return 'Hello World!'

#desde cualquier direccion
app.run(host='0.0.0.0',port=81)