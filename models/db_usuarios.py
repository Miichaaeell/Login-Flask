from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv
banco = getenv('MEU_BANCO')
db = create_engine(banco)
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuarios'
    Nome = Column("nome", String(42), nullable=True )
    Sexo = Column("Sexo", String(42), nullable=True )
    Data_Nascimento = Column("Data_Nascimento", String, nullable=True )
    Email = Column("Email", String, nullable=True )
    Telefone = Column("Telefone", String, nullable=True )
    Rua = Column("Rua", String, nullable=True )
    Numero_casa = Column("Numero_casa", Integer, nullable=True )
    Bairro = Column("Bairro", String,nullable=True )
    CEP = Column("CEP", Integer, nullable=True )
    Usuario = Column("Usuario", String, primary_key=True, nullable=True )
    Senha = Column("Senha", String, nullable=True )
    Status = Column("Status", String )

    def __init__(self, Nome, Sexo, Data_Nascimento, Email, Telefone, Rua, Numero_casa, Bairro, CEP, Usuario, Senha):
        self.Nome = Nome
        self.Sexo = Sexo
        self.Data_Nascimento = Data_Nascimento
        self.Email = Email
        self.Telefone = Telefone
        self.Rua = Rua
        self.Numero_casa = Numero_casa
        self.Bairro = Bairro
        self.CEP = CEP
        self.Usuario = Usuario
        self.Senha = Senha
        
Base.metadata.create_all(bind=db)

def receber_formulario(formulario, usuario):
    dados = []
    for v in formulario:
        dados.append(v)
    user = {
        "Nome": dados[0],
        "Sexo" : dados[1],
        "Data_Nascimento": dados[2],
        "Email": dados[3],
        "Telefone": dados[4],
        "Rua": dados[5],
        "Numero_casa": dados[6],
        "Bairro": dados[7],
        "CEP": dados[8],
    }
    usuario.Nome = user["Nome"]
    usuario.Sexo = user["Sexo"]
    usuario.Data_Nascimento = user["Data_Nascimento"]
    usuario.Email = user["Email"]
    usuario.Telefone = user["Telefone"]
    usuario.Rua = user["Rua"]
    usuario.Numero_casa = user["Numero_casa"]
    usuario.Bairro = user["Bairro"]
    usuario.CEP = user["CEP"]
    return usuario

def analisar_formulario(formulario):
    dados = []
    for v in formulario:
        dados.append(v)
    user = {
        "Nome": dados[0],
        "Sexo" : dados[1],
        "Data_Nascimento": dados[2],
        "Email": dados[3],
        "Telefone": dados[4],
        "Rua": dados[5],
        "Numero_casa": dados[6],
        "Bairro": dados[7],
        "CEP": dados[8],
        "Usuario": dados[9],
        "Senha": dados[10]
    }
    usuario = Usuario(user["Nome"], user["Sexo"], user["Data_Nascimento"], user["Email"], user["Telefone"], user["Rua"], user["Numero_casa"], user["Bairro"], user["CEP"], user["Usuario"], user["Senha"])
    return usuario
