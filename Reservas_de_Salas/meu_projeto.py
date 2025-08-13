import csv # importa módulo padrão do Python usado para criar, ler e manipular arquivos CSV
import os  # Importa o módulo os para verificar se o arquivo já existe
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DADOS_DIR = os.path.join(BASE_DIR, 'dados')
os.makedirs(DADOS_DIR, exist_ok=True)  # Garante que a pasta 'dados' existe

class Usuario:
    def __init__(self, nome, data_nascimento, contato_email, contato_telefone):
        self.nome = nome
        self.data_nasc = data_nascimento
        self.cont_email = contato_email
        self.cont_tel = contato_telefone
        self.id = 0
    
    def __eq__(self, outro):
        return self.cont_email == outro.cont_email
    
    def __repr__(self):
        return f"ID:{self.id}, Nome:{self.nome}, Data nascimento:{self.data_nasc}, Tel:{self.cont_tel}, e-mail:{self.cont_email}"
class Arquivo_usuarios:
    def __init__(self):
        self.cadastro_usuarios = []
        self.proximo_id = 1
        self.agora = datetime.now()

    def carregar_usuarios_csv(self):
        usuarios_csv_path = os.path.join(DADOS_DIR, 'usuarios.csv')
        if os.path.isfile(usuarios_csv_path):
            with open(usuarios_csv_path, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    usuario = Usuario(
                        nome=row["Nome"],
                        data_nascimento=row["Data de Nascimento"],
                        contato_email=row["E-mail"],
                        contato_telefone=row["Telefone"]
                    )
                    usuario.id = int(row["ID"])
                    self.cadastro_usuarios.append(usuario)
                    self.proximo_id = max(self.proximo_id, usuario.id + 1)

    def adicionar_usuario(self, usuario):
        if usuario in self.cadastro_usuarios:
            print("Usuário já cadastrado.")
        else:
            usuario.id = self.proximo_id
            self.proximo_id += 1
            self.cadastro_usuarios.append(usuario)
            print("Cadastro realizado com sucesso.")
            usuarios_csv_path = os.path.join(DADOS_DIR, 'usuarios.csv')  # Nome do arquivo CSV onde os usuários serão salvos
            arquivo_existe = os.path.isfile(usuarios_csv_path)  # Verifica se o arquivo já existe
            with open(usuarios_csv_path, "a", newline="") as csvfile:  # Abre o arquivo em modo append (adicionar)
                writer = csv.writer(csvfile)  # Cria o escritor CSV
                if not arquivo_existe:  # Se o arquivo não existe, escreve o cabeçalho
                    writer.writerow(["ID", "Nome", "Data de Nascimento", "Telefone", "E-mail", "Data de Cadastro"])
                writer.writerow([usuario.id, usuario.nome, usuario.data_nasc, usuario.cont_tel, usuario.cont_email, self.agora])  # Escreve os dados do usuário

    def excluir_usuario(self, identificacao):   
        self.cadastro_usuarios = [c for c in self.cadastro_usuarios if c.id != identificacao]
        usuarios_csv_path = os.path.join(DADOS_DIR, 'usuarios.csv')
        with open(usuarios_csv_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Nome", "Data de Nascimento", "Telefone", "E-mail"])  # Cabeçalho
            for usuario in self.cadastro_usuarios:
                writer.writerow([usuario.id, usuario.nome, usuario.data_nasc, usuario.cont_tel, usuario.cont_email])
 
class Sala:
    def __init__(self, numero, capacidade):
        self.num_sala = numero   # total de 10 salas
        self.capacidade =  capacidade  # (sa = sala, pe = pessoas) sendo 5sa para 5pe, 4sa para 12pe e 1sa para 30pe
        self.codigo = 0
    
    def __eq__(self, outro):
        return self.num_sala == outro.num_sala
    
    def __repr__(self):
        return f"Código de reserva:{self.codigo}, Numero da sala:{self.num_sala}, Capacidade da sala:{self.capacidade}"
    
salas_disponiveis = [
    Sala(1, 5), Sala(2, 5), Sala(3, 5), Sala(4, 5), Sala(5, 5),
    Sala(6, 12), Sala(7, 12), Sala(8, 12), Sala(9, 12),
    Sala(10, 30)
]

class Reserva_sala:
    def __init__(self):
        self.reserva = []
        self.proximo_codigo = 1
    
    def cadastrar_reserva(self,reservado):
        if reservado in self.reserva:
            print("Sala indisponivel.")
        else:
            reservado.codigo = self.proximo_codigo
            self.proximo_codigo += 1
            self.reserva.append(reservado)
            agora = datetime.now()  # Captura a data e hora atual
            print(f"Reserva realizada com sucesso em {agora}.")

    def excluir_reserva(self, identifica):
        self.reserva = [c for c in self.reserva if c.codigo != identifica]