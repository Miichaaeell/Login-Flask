import mysql.connector
from time import localtime
class Cliente:
    def __init__(self, nome, sexo, data_nascimento, email, telefone, rua, numero_casa, bairro, cep, usuario, senha, status ):
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
        self.status = status

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
    comando = f'INSERT INTO `Inscritos` (`Nome`,`Sexo`, `Data_Nascimento`, `E-mail`, `Telefone`, `Rua`, `Numero_casa`, `Bairro`, `CEP`, `Usuario`, `Senha`, `Status`) VALUES  ("{cliente.nome}", "{cliente.sexo}", "{cliente.data_nascimento}", "{cliente.email}", "{cliente.telefone}", "{cliente.rua}", "{cliente.numero_casa}", "{cliente.bairro}", "{cliente.cep}", "{cliente.usuario}", "{cliente.senha}", "{cliente.status}")'
    alterar_db(comando)

def exlcluir(usuario):
    alterar_db(f'DELETE FROM Inscritos WHERE Usuario = "{usuario}"')
    return f'{usuario} excluido'

def verificar_cadastro(nome_usuario):
    usuarios = visualizar_db('SELECT Usuario  FROM Inscritos')
    validado = False
    for usuario in usuarios:
        if usuario[0] == nome_usuario:
            validado = True
    return validado

def logar(usuario, senha):
    acesso = False
    dados_db = visualizar_db('SELECT `Usuario`, `Senha`, `Status` FROM Inscritos')
    for cliente in dados_db:
        if usuario == cliente[0] and senha == cliente[1]:
            acesso = True
            alterar_db(f' UPDATE `Inscritos` SET `Status` = "logado" WHERE (`Usuario` = "{cliente[0]}") ')      
    return acesso

def logado(usuario):
    dados = visualizar_db(f'SELECT * FROM Inscritos WHERE Usuario = "{usuario}"')
    cliente = Cliente(dados[0][0], dados[0][1], dados[0][2], dados[0][3], dados[0][4], dados[0][5], dados[0][6], dados[0][7], dados[0][8], dados[0][9], dados[0][10], dados[0][11])
    return cliente

def deslogar(usuario):
    alterar_db(f' UPDATE `Inscritos` SET `Status` = "deslogado" WHERE (`Usuario` = "{usuario}" ) ')
