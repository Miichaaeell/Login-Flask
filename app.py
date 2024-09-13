from flask import Flask, render_template, request, redirect
from time import localtime
from funcoesbd import Cliente, inserir, validar, logar, logado

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
@app.route('/login_fail')
def login_fail():
    return render_template('login_fail.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrado', methods=['POST'])
def cadastrado():
    query = request.form.values()
    dados = []
    for v in query:
        dados.append(v)
    cliente = Cliente(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], dados[8], dados[9],  dados[10])
    validacao = validar(cliente.usuario)
    if validacao == False:
        inserir(cliente)
        return render_template('cadastrado.html', nome = dados[0])
        
    else: 
        return redirect('cadastro')

    
@app.route('/painel', methods=['POST'])
def meu_painel():
    usuario = request.form.get('user')
    senha = request.form.get('senha')
    acesso = logar(usuario, senha)
    if acesso == True:
        horario = localtime()
        hora = horario[3]
        saudação = ''
        if hora > 0 and hora < 12:
            saudação = 'Bom dia!'
        elif hora > 12 and hora < 18:
            saudação = 'Boa tarde'
        else:
            saudação = 'Boa noite'
        dados_usuario = logado(usuario)
        return render_template('painel.html', saudação = saudação, nome = dados_usuario[0])
    else:

        return redirect('login_fail')

if __name__ == '__main__':
    app.run(debug=True)