from main import app
from flask import render_template, request, redirect
from funcoesbd import inserir_usuario, logar, verificar_cadastro, analisar_formulario, visualizar_db, alterar_db

@app.route('/', methods=["GET", "POST"])
def index():
    metodo = request.method
    if metodo == "GET":
        return render_template('index.html')
    else:
        usuario = request.form.get('user')
        senha = request.form.get('senha')
        print(usuario, senha)
        alterar_db(f'UPDATE `Inscritos` SET `Senha` = "{senha}" WHERE (`Usuario` = "{usuario}") ')
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

@app.route('/cadastro',  methods=["GET", 'POST'])
def cadastro():
    metodo = request.method
    if metodo == "GET":
        return render_template('cadastro.html')
    else:
        return render_template('cadastro.html', erro ='Usuário já cadastrado')

@app.route('/cadastrado', methods=['POST'])
def cadastrado():
    formulario = request.form.values()
    cliente = analisar_formulario(formulario)
    cadastro = verificar_cadastro(cliente.usuario)
    if cadastro == False:
        inserir_usuario(cliente)
        return render_template('cadastrado.html', nome = cliente.nome)
        
    else: 
        return redirect('cadastro')

@app.route('/recuperar_senha')
def recuperar_senha():
    return render_template('recuperar_senha.html')

@app.route('/recuperar_senha2', methods=['POST'])
def recuperar_senha2():
    usuario = request.form.get('usuario')
    db = visualizar_db('SELECT `Usuario` FROM Inscritos')
    continuar = False
    for valor in db:
        if usuario == valor[0]:
            continuar = True
    if continuar == True:
        return render_template('recuperar_senha2.html', user = usuario)
    else:
        return render_template('recuperar_senha.html', msg = 'Usuario não encontrado')
