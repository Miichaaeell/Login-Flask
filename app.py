from flask import Flask, render_template, request
from time import localtime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrado', methods=['POST'])
def cadastrado():
    nome = request.form.get('nome')
    return render_template('cadastrado.html', nome = nome)
@app.route('/painel', methods=['POST'])
def meu_painel():
    horario = localtime()
    hora = horario[3]
    saudação = ''
    if hora > 0 and hora < 12:
        saudação = 'Bom dia!'
    elif hora > 12 and hora < 18:
        saudação = 'Boa tarde'
    else:
        saudação = 'Boa noite'    
    nome = request.form.get('user')
    return render_template('painel.html', saudação = saudação,nome = nome)

if __name__ == '__main__':
    app.run(debug=True)