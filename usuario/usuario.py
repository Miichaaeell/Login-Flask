from flask import render_template, request, redirect, Blueprint
from models.db_usuarios import session, Usuario, receber_formulario
import requests
from time import localtime

usuarios = Blueprint('usuario', __name__, template_folder='templates', static_folder='static')
    
@usuarios.route('/<user>/painel', methods=['GET', 'POST'])
def painel(user):
    usuario = session.query(Usuario).filter_by(Usuario = user).first()
    saudação = ''
    horario = localtime()
    hora =  horario[3]
    if hora > 0 and hora < 12:
        saudação = 'Bom dia!'
    elif hora >= 12 and hora < 18:
        saudação = 'Boa tarde'
    else:
        saudação = 'Boa noite'
    if request.method == 'GET':
        if usuario.Status == 'logado':         
            return render_template('painel.html', saudação = saudação, nome = usuario.Nome, user= usuario.Usuario, sexo = usuario.Sexo, nascimento = usuario.Data_Nascimento, email = usuario.Email, telefone = usuario.Telefone, rua = usuario.Rua, numero_casa = usuario.Numero_casa, bairro=usuario.Bairro, CEP = usuario.CEP)
        else:
            return redirect('/login')
    else:
        formulario = request.form.values()
        usuario = session.query(Usuario).filter_by(Usuario = user).first()
        usuario = receber_formulario(formulario, usuario)
        session.add(usuario)
        session.commit()
        return render_template('painel.html', saudação = saudação, nome = usuario.Nome, user= usuario.Usuario, sexo = usuario.Sexo, nascimento = usuario.Data_Nascimento, email = usuario.Email, telefone = usuario.Telefone, rua = usuario.Rua, numero_casa = usuario.Numero_casa, bairro=usuario.Bairro, CEP = usuario.CEP)

@usuarios.route('/<user>', methods=['GET', 'POST'])
def index_usuario(user):
    metodo = request.method
    usuario = session.query(Usuario).filter_by(Usuario = user).first()
    if metodo == 'GET':
        if usuario.Status == 'logado':
            return render_template('index_user.html', user = usuario.Usuario)
        else:
            return redirect('/login')
    elif metodo == "POST":
        senha  = request.form.get('nova_senha')
        usuario.Senha = senha
        session.add(usuario)
        session.commit()
        return redirect('/login')

@usuarios.route('/logout/<user>')
def logout(user):
    usuario = session.query(Usuario).filter_by(Usuario = user).first()
    usuario.Status = "Deslogado"
    session.add(usuario)
    session.commit()
    return redirect('/')

@usuarios.route('/<user>/delete')
def delete(user):
    usuario = session.query(Usuario).filter_by(Usuario = user).first()
    if usuario.Status == "logado":
        session.delete(usuario)
        session.commit()
    return redirect('/')

@usuarios.route('/<user>/alterar_senha')
def alterar_senha(user):
    usuario = session.query(Usuario).filter_by(Usuario = user).first()
    if usuario.Status == "logado":
        return render_template('alterar_senha.html', user = usuario.Usuario)
    else:
        return redirect('/')

@usuarios.route('/<user>/alterar_dados')
def alterar_dados(user):
    usuario = session.query(Usuario).filter_by(Usuario = user).first()
    if usuario.Status == "logado":
        return render_template('alterar_dados.html', user= usuario.Usuario, nome = usuario.Nome, nascimento = usuario.Data_Nascimento, email = usuario.Email, telefone= usuario.Telefone, rua = usuario.Rua, numero = usuario.Numero_casa, bairro = usuario.Bairro, cep = usuario.CEP, sexo = usuario.Sexo)
    else:
        return redirect('/')
    
@usuarios.route('/<user>/galeria')
def galeria(user):
    usuario = session.query(Usuario).filter_by(Usuario = user).first()
    if usuario.Status == 'logado':
        return render_template('galeria.html', user =  user)
    else:
        return redirect('/')
    
@usuarios.route('/<user>/cotar_moeda')
def cotar_moeda(user):
    requisição = requests.get(f'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    retorno = requisição.json() 
    dolar = f'{float(retorno["USDBRL"]["bid"]):,.2f}'
    euro = f'{float(retorno["EURBRL"]["bid"]):,.2f}'
    bitcoin = f'{float(retorno["BTCBRL"]["bid"]):,.2f}'
    return render_template('cotar_moeda.html', dolar = dolar, euro = euro, bitcoin = bitcoin, user = user)
    