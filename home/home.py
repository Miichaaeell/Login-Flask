from flask import render_template, request, redirect, Blueprint
from models.db_usuarios import session, analisar_formulario, Usuario

home = Blueprint('home', __name__,template_folder='templates')
@home.route('/', methods=["GET", "POST"])
def index():
    metodo = request.method
    if metodo == "GET":
        return render_template('index.html')
    elif metodo == "POST":
        user = request.form.get('user')
        senha = request.form.get('senha')
        usuario = session.query(Usuario).filter_by(Usuario = user).first()

        usuario.Senha = senha
        session.add(usuario)
        session.commit()
        return render_template('index.html')



@home.route('/login', methods=["GET", "POST"])
def login():
    metodo = request.method
    if metodo == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        senha = request.form.get('senha')
        usuario = session.query(Usuario).filter_by(Usuario = user).first()
        if not usuario:
            return render_template('login.html', status = "Usuario Não encontrado")
        elif usuario.Senha != senha:
            return render_template('login.html', status = "Senha Incorreta")
        else:
            usuario.Status = "logado"
            session.add(usuario)
            session.commit()
            return redirect(f'{usuario.Usuario}')

@home.route('/cadastro',  methods=["GET", 'POST'])
def cadastro():
    metodo = request.method
    if metodo == "GET":
        return render_template('cadastro.html')
    else:
        return render_template('cadastro.html', erro ='Usuário já cadastrado')

@home.route('/cadastrado', methods=['POST'])
def cadastrado():
    formulario = request.form.values()
    user = analisar_formulario(formulario)
    usuario = session.query(Usuario).filter_by(Usuario = user.Usuario).first()
    if not usuario:
        session.add(user)
        session.commit()
        return render_template('cadastrado.html', nome = user.Nome)
        
    else: 
        return redirect('cadastro', code=307)

@home.route('/recuperar_senha')
def recuperar_senha():
    return render_template('recuperar_senha.html')

@home.route('/recuperar_senha2', methods=['POST'])
def recuperar_senha2():
    user = request.form.get('usuario')
    usuario = session.query(Usuario).filter_by(Usuario = user).first()
    if not usuario:
        return render_template('recuperar_senha.html', msg = 'Usuario não encontrado')
    else:
        return render_template('recuperar_senha2.html', user = usuario.Usuario)
      
