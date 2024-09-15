from flask import Flask, render_template, request, redirect
from time import localtime
from funcoesbd import Cliente, inserir, logar, logado, deslogar,verificar_cadastro, exlcluir

app = Flask(__name__)

#Rotas Home
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    metodo = request.method
    if metodo == "GET":
        return render_template('login.html')
    else:
        usuario = request.form.get('user')
        senha = request.form.get('senha')
        acesso = logar(usuario, senha)
        if acesso == True:
            return redirect(f'{usuario}')
        else:
            return render_template('login.html', status = "Usuario ou Senha Incorretos")
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrado', methods=['POST'])
def cadastrado():
    query = request.form.values()
    dados = []
    for v in query:
        dados.append(v)
        
    print(dados)
    cliente = Cliente(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], dados[8], dados[9],  dados[10], 'deslogado')
    cadastro = verificar_cadastro(cliente.usuario)
    if cadastro == False:
        inserir(cliente)
        return render_template('cadastrado.html', nome = dados[0])
        
    else: 
        return redirect('cadastro')

#Rotas Usuario
    
@app.route('/<user>/painel')
def painel(user):
    dados_usuario = logado(user)
    if dados_usuario.status == 'logado':
        saudação = ''
        horario = localtime()
        hora =  horario[3]
        if hora > 0 and hora < 12:
            saudação = 'Bom dia!'
        elif hora >= 12 and hora < 18:
            saudação = 'Boa tarde'
        else:
            saudação = 'Boa noite'
        
        return render_template('painel.html', saudação = saudação, nome = dados_usuario.nome, user= dados_usuario.usuario, sexo = dados_usuario.sexo, nascimento = dados_usuario.data_nascimento, email = dados_usuario.email, telefone = dados_usuario.telefone, rua = dados_usuario.rua, numero_casa = dados_usuario.numero_casa, bairro=dados_usuario.bairro, CEP = dados_usuario.cep)
    else:
        return redirect('/login')

@app.route('/<user>')
def index_usuario(user):
    dados_usuario = logado(user)
    if dados_usuario.status == 'logado':
        return render_template('index_user.html', user = dados_usuario.usuario)
    else:
        return redirect('/login')

@app.route('/logout/<usuario>')
def logout(usuario):
    deslogar(usuario)
    return redirect('/')

@app.route('/<usuario>/delete')
def delete(usuario):
    exlcluir(usuario)
    return redirect('/')

@app.route('/<usuario>/alterar_senha')
def alterar_senha(usuario):
    return "alterar senha em construção"

@app.route('/<usuario>/alterar_dados')
def alterar_dados(usuario):
    return "alterar dados em construção"


if __name__ == '__main__':
    app.run(debug=True)