from main import app
from flask import render_template, request, redirect
from time import localtime
from funcoesbd import  dados_usuario, deslogar, exlcluir_usuario, alterar_db, analisar_formulario, atualizar_usuario

    
@app.route('/<user>/painel', methods=['GET', 'POST'])
def painel(user):
    metodo = request.method
    usuario = dados_usuario(user)
    saudação = ''
    horario = localtime()
    hora =  horario[3]
    if hora > 0 and hora < 12:
        saudação = 'Bom dia!'
    elif hora >= 12 and hora < 18:
        saudação = 'Boa tarde'
    else:
        saudação = 'Boa noite'
    if metodo == 'GET':
        if usuario.status == 'logado':         
            return render_template('painel.html', saudação = saudação, nome = usuario.nome, user= usuario.usuario, sexo = usuario.sexo, nascimento = usuario.data_nascimento, email = usuario.email, telefone = usuario.telefone, rua = usuario.rua, numero_casa = usuario.numero_casa, bairro=usuario.bairro, CEP = usuario.cep)
        else:
            return redirect('/login')
    else:
        formulario = request.form.values()
        dados = analisar_formulario(formulario)
        atualizar_usuario(dados, user)
        usuario = dados_usuario(user)
        return render_template('painel.html', saudação = saudação, nome = usuario.nome, user= usuario.usuario, sexo = usuario.sexo, nascimento = usuario.data_nascimento, email = usuario.email, telefone = usuario.telefone, rua = usuario.rua, numero_casa = usuario.numero_casa, bairro=usuario.bairro, CEP = usuario.cep)

@app.route('/<user>', methods=['GET', 'POST'])
def index_usuario(user):
    metodo = request.method
    if metodo == 'GET':
        usuario = dados_usuario(user)
        if usuario.status == 'logado':
            return render_template('index_user.html', user = usuario.usuario)
        else:
            return redirect('/login')
    else:
        senha  = request.form.get('nova_senha')
        alterar_db(f'UPDATE `Inscritos` SET `Senha` = "{senha}" WHERE (`Usuario` = "{user}") ')
        deslogar(user)
        return redirect('/login')

@app.route('/logout/<usuario>')
def logout(usuario):
    deslogar(usuario)
    return redirect('/')

@app.route('/<usuario>/delete')
def delete(usuario):
    usuario = dados_usuario(usuario)
    if usuario.status == "logado":
        exlcluir_usuario(usuario)
    return redirect('/')

@app.route('/<usuario>/alterar_senha')
def alterar_senha(usuario):
    usuario = dados_usuario(usuario)
    if usuario.status == "logado":
        return render_template('alterar_senha.html', user = usuario.usuario)
    else:
        return redirect('/')

@app.route('/<usuario>/alterar_dados')
def alterar_dados(usuario):
    usuario = dados_usuario(usuario)
    if usuario.status == "logado":
        return render_template('alterar_dados.html', user= usuario.usuario, nome = usuario.nome, nascimento = usuario.data_nascimento, email = usuario.email, telefone= usuario.telefone, rua = usuario.rua, numero = usuario.numero_casa, bairro = usuario.bairro, cep = usuario.cep )
    else:
        return redirect('/')