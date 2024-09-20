from flask import Flask

app = Flask(__name__)


from routes.home import *
from routes.usuario import *

if __name__ == '__main__':
    app.run(debug=True)