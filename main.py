from flask import Flask
from usuario.usuario import usuarios
from home.home import home

app = Flask(__name__)
app.register_blueprint(usuarios)
app.register_blueprint(home)
if __name__ == '__main__':
    app.run(debug=True)