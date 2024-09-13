import mysql.connector
class Cliente:
    def __init__(self, nome, sexo, data_nascimento, email, telefone, rua, numero_casa, bairro, cep, usuario, senha ):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone
        self.rua = rua
        self.numero_casa = numero_casa
        self.bairro = bairro
        self.cep = cep
        self.usuario = usuario
        self.senha = senha

def alterar_db(comando):
    conexao = mysql.connector.connect(user='root', database='cadastro_site')
    cursor = conexao.cursor()
    comando = f'{comando}'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

def visualizar_db(comando):
    conexao = mysql.connector.connect(user='root', database='cadastro_site')
    cursor = conexao.cursor()
    comando = f'{comando}'
    cursor.execute(comando)
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return dados

def inserir (cliente):
    comando = f'INSERT INTO `Inscritos` (`Nome`,`Sexo`, `Data_Nascimento`, `E-mail`, `Telefone`, `Rua`, `Numero_casa`, `Bairro`, `CEP`, `Usuario`, `Senha`) VALUES  ("{cliente.nome}", "{cliente.sexo}", "{cliente.data_nascimento}", "{cliente.email}", "{cliente.telefone}", "{cliente.rua}", "{cliente.numero_casa}", "{cliente.bairro}", "{cliente.cep}", "{cliente.usuario}", "{cliente.senha}")'
    alterar_db(comando)

def exlcluir(usuario):
    alterar_db(f'DELETE FROM Inscritos WHERE Usuario = "{usuario}"')
    return f'{usuario} excluido'

def validar(nome_usuario):
    usuarios = visualizar_db('SELECT Usuario  FROM Inscritos')
    validado = False
    for usuario in usuarios:
        if usuario[0] == nome_usuario:
            validado = True
    return validado

def logar(usuario, senha):
    acesso = False
    dados_db = visualizar_db('SELECT `Usuario`, `Senha` FROM Inscritos')
    for cliente in dados_db:
        if usuario == cliente[0] and senha == cliente[1]:
            acesso = True
    return acesso

def logado(usuario):
    dados_usuario = visualizar_db(f'SELECT * FROM Inscritos WHERE Usuario = "{usuario}"')
    return dados_usuario[0]
