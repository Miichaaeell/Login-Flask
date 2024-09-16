import mysql.connector
from time import localtime
class Usuarios:
    def __init__(self, nome, sexo, data_nascimento, email, telefone, rua, numero_casa, bairro, cep, usuario = '', senha = '', status = '' ):
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
#manipular Db
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


# Manipular dados usuario
def inserir_usuario (usuario):
    comando = f'INSERT INTO `Inscritos` (`Nome`,`Sexo`, `Data_Nascimento`, `E-mail`, `Telefone`, `Rua`, `Numero_casa`, `Bairro`, `CEP`, `Usuario`, `Senha`, `Status`) VALUES  ("{usuario.nome}", "{usuario.sexo}", "{usuario.data_nascimento}", "{usuario.email}", "{usuario.telefone}", "{usuario.rua}", "{usuario.numero_casa}", "{usuario.bairro}", "{usuario.cep}", "{usuario.usuario}", "{usuario.senha}", "{usuario.status}")'
    alterar_db(comando)

def atualizar_usuario(usuario, user):
    comando = f' UPDATE `Inscritos` SET `Nome` = "{usuario.nome}", `Sexo` = "{usuario.sexo}", `Data_Nascimento` = "{usuario.data_nascimento}", `E-mail` = "{usuario.email}", `Telefone` = "{usuario.telefone}", `Rua` = "{usuario.rua}", `Numero_casa` = "{usuario.numero_casa}", `Bairro` = "{usuario.bairro}", `CEP` = "{usuario.cep}" WHERE  (`Usuario` = "{user}" )'
    print(user)
    alterar_db(comando)

def exlcluir_usuario(usuario):
    alterar_db(f'DELETE FROM Inscritos WHERE Usuario = "{usuario}"')


def dados_usuario(usuario):
    dados = visualizar_db(f'SELECT * FROM Inscritos WHERE Usuario = "{usuario}"')
    usuario = Usuarios(dados[0][0], dados[0][1], dados[0][2], dados[0][3], dados[0][4], dados[0][5], dados[0][6], dados[0][7], dados[0][8], dados[0][9], dados[0][10], dados[0][11])
    return usuario



def logar(usuario, senha):
    acesso = False
    dados_db = visualizar_db('SELECT `Usuario`, `Senha`, `Status` FROM Inscritos')
    for dado in dados_db:
        if usuario == dado[0] and senha == dado[1]:
            acesso = True
            alterar_db(f' UPDATE `Inscritos` SET `Status` = "logado" WHERE (`Usuario` = "{dado[0]}") ')      
    return acesso


def deslogar(usuario):
    alterar_db(f' UPDATE `Inscritos` SET `Status` = "deslogado" WHERE (`Usuario` = "{usuario}" ) ')

#  Validação de formularios
def verificar_cadastro(nome_usuario):
    usuarios = visualizar_db('SELECT Usuario  FROM Inscritos')
    validado = False
    for usuario in usuarios:
        if usuario[0] == nome_usuario:
            validado = True
    return validado


def analisar_formulario(formulario):
    dados = []
    for v in formulario:
        dados.append(v)
    usuario = Usuarios(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], dados[8])
    return usuario