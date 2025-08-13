from meu_projeto import Usuario, Arquivo_usuarios, Sala, Reserva_sala, salas_disponiveis
from datetime import datetime

arquivo_usuarios = Arquivo_usuarios()
arquivo_usuarios.carregar_usuarios_csv()
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
        data_nascimento = input("Data de nascimento: ")
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
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