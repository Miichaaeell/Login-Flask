from flask import Flask, render_template, request

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
    nome = request.form.get('user')
    return render_template('cadastrado.html', nome = nome)
@app.route('/painel', methods=['POST'])
def meu_painel():
    nome = request.form.get('user')
    return render_template('painel.html', nome = nome)

if __name__ == '__main__':
    app.run(debug=True)