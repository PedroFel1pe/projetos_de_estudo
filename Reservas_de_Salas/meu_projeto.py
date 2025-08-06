from datetime import datetime

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
        
    def adicionar_usuario(self, usuario):
        if usuario in self.cadastro_usuarios:
            print("Usuário já cadastrado.")
        else:
            usuario.id = self.proximo_id
            self.proximo_id += 1
            self.cadastro_usuarios.append(usuario)
            print("Cadastro realizado com sucesso.")
        
    def excluir_usuario(self, identificacao):
        self.cadastro_usuarios = [c for c in self.cadastro_usuarios if c.id != identificacao]
 
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
            print("Reserva feita com sucesso.")

    def excluir_reserva(self, identifica):
        self.reserva = [c for c in self.reserva if c.codigo != identifica]

arquivo_usuarios = Arquivo_usuarios()
reserva_sala = Reserva_sala()

while True:
    print(
        """
    ===============MENU===============

    1-Cadastrar usuário
    2-Cadastrar reserva de sala
    3-Verificar usuários
    4-Verificar reservas
    5-Cancelar reserva
    6-Excluir cadastro de usuário
    0-Sair do sistema

    ==================================
    """
    )
    menu = input("Selecione uma opção(0 a 6):")

    print("=" * 34)

    if menu == "1":
        print("CADASTRO")

        nome = input("Nome de usuário: ")
        data_nascimento = int(input("Data de nascimento: "))
        contato_email = input("e-mail: ")
        contato_telefone = int(input("Telefone: "))
        usuario = Usuario(nome, data_nascimento, contato_email, contato_telefone)
        arquivo_usuarios.adicionar_usuario(usuario)

    elif menu == "2":
        print("CADASTRAR RESERVA DE SALA")
        print("Salas de 1 a 5, capacidade para 5 pessoas")
        print("Salas de 6 a 9, capacidade para 12 pessoas")
        print("Sala 10, capacidade para 30 pessoas")
        opcao_reserva = int(input("Qual sala deseja (1 a 10):"))
        
        sala_escolhida = None
        for sala in salas_disponiveis:
            if sala.num_sala == opcao_reserva:
                sala_escolhida = sala
                break
        if sala_escolhida:
            reserva_sala.cadastrar_reserva(sala_escolhida)
        else:
            print("Sala não encontrada")

    elif menu == "3":
        for contato in arquivo_usuarios.cadastro_usuarios:
            print(contato.__repr__())

    elif menu == "4":
        for sala in reserva_sala.reserva:
            print(sala.__repr__())

    elif menu == "5":
        identifica = int(input("Informe o código da reserva a ser excluida:"))
        reserva_sala.excluir_reserva(identifica)
        print("Reserva removida")

    elif menu == "6":
        identificacao = int(input("Informe o ID do usuário a ser excluido:"))
        arquivo_usuarios.excluir_usuario(identificacao)
        print("Contato removido")

    elif menu == "0":
        print("Encerrando sistema....")
        break

    else:
        print("Opção invalida.")