from random import randint
import os
import msvcrt

def menu():
    print("""MACK BANK – ESCOLHA UMA OPÇÃO
          
    (1) CADASTRAR CONTA CORRENTE
    (2) DEPOSITAR
    (3) SACAR
    (4) CONSULTAR SALDO
    (5) CONSULTAR EXTRATO
    (6) FINALIZAR
    """)

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("cls")

def cadastro_cliente(dados_cliente):

    def gerar_conta():
        # randint -> Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
        conta = randint(1000, 9999)
        return conta

    # aqui nessa parte eu adiciono o número da conta na lista com os dados do cliente:
    dados_cliente.append(gerar_conta())

    def conta():

        while True: 

            limpar_tela()

            print("Mack Bank - Cadastro de Conta\n")
            print(f"Número da Conta: {dados_cliente[0]}")
            
            # nome do cliente
            try: 
                print(f"Nome do Cliente: {dados_cliente[1]}")
            except:
                nome_cliente = input("Nome do Cliente: ")

                if nome_cliente.strip() == "": 
                    print("O nome do cliente precisa ser preenchido. Pressione alguma tecla para prosseguir...")
                    msvcrt.getch()
                    continue
                elif nome_cliente.strip().isnumeric(): 
                    print("O nome do cliente não pode ser numérico. Pressione alguma tecla para prosseguir...")
                    msvcrt.getch()
                    continue

                dados_cliente.append(nome_cliente)

            # telefone
            try:
                print(f"Telefone.......: {dados_cliente[2]}")
            except:
                try:
                    telefone = int(input("Telefone.......: "))
                    dados_cliente.append(telefone)
                except:
                    print("Digite um valor correto para o telefon. Pressione alguma tecla para prosseguir...")
                    msvcrt.getch()
                    continue

            # e-mail
            try: 
                print(f"E-mail..........: {dados_cliente[3]}")
            except:
                email = input("E-mail..........: ")

                email = email.strip()
                if not "@" in email or not "." in email: 
                    print("Email Inválido! Pressione alguma tecla para prosseguir...")
                    msvcrt.getch()
                    continue

                dados_cliente.append(email)

            # saldo inicial
            try:
                print(f"Saldo Inicial...: R$ {dados_cliente[4]}")
            except:
                try:
                    saldo_inical = float(input("Saldo Inicial...: R$ "))
                    if saldo_inical < 1000: raise 
                    dados_cliente.append(saldo_inical)
                except:
                    print("O saldo inicial precisa ser numérico e maior que 1000. Pressione alguma tecla para prosseguir...") 
                    msvcrt.getch()
                    continue

            # limite de crédito
            try:
                print(f"Limite de Crédito: R$ {dados_cliente[5]}")
            except:
                try:
                    limite_credito = float(input("Limite de Crédito: R$ "))
                    dados_cliente.append(limite_credito)
                except:
                    print("O valor precisa ser numérico e maior ou igual a 0. Pressione alguma tecla para prosseguir...")
                    msvcrt.getch()
                    continue
            # senha
            senha = input(f"Senha............: ")

            if len(senha) != 6: 
                print("A senha precisa ter 6 caracteres. Pressione alguma tecla para prosseguir...")
                msvcrt.getch()
                continue
            else: 
                confirmacao_senha = input("Repita a Senha...: ")
                if senha != confirmacao_senha: 
                    print("As senhas precisam ser iguais! Pressione alguma tecla para prosseguir...")
                    msvcrt.getch()
                    continue
                else:
                    dados_cliente.append(senha)
                    break
    conta()

    input("\nCadastro realizado! Pressione ENTER voltar ao menu...")
    return dados_cliente

def deposito(dados_cliente, saques_depositos):

    limpar_tela()

    print("MACK BANK – DEPÓSITO DA CONTA\n")

    # verifico se o formato dos números são validos e se o funcionamento está certo.
    try:
        numero_conta = int(input("Informe o número da conta: "))

        if (numero_conta == dados_cliente[0]) == False: raise ValueError("Conta não encontrada.")
                    
        print(f"Nome do Cliente: {dados_cliente[1]}")

        valor_deposito = float(input("Digite o valor do depósito: "))

        if valor_deposito <= 0:
            raise ValueError("Digite um valor maior do que 0.")
        
        dados_cliente[4] = dados_cliente[4] + valor_deposito
        saques_depositos.append(valor_deposito)

        input("\nDepósito realizado com sucesso! Pressione alguma ENTER para prosseguir.")
        
    except ValueError as e:
        input(f"{e} Pressione ENTER para tentar novamente...")
        deposito(dados_cliente, saques_depositos)

    except Exception as e:
        input(f"{e} Pressione ENTER para tentar novamente...")
        deposito(dados_cliente, saques_depositos)

    return dados_cliente, saques_depositos

def saque(dados_cliente, saques_depositos):
    
    limpar_tela()

    print("MACK BANK – SAQUE EM CONTA")

    numero_conta = int(input("INFORME O NÚMERO DA CONTA: "))

    if (numero_conta == dados_cliente[0]):
        print(f"NOME DO CLIENTE: {dados_cliente[1]}")

        senha = input("INFORME A SENHA: ")
    
        if senha == dados_cliente[6]:
            tentativa_senha = 1
            valor_saque = float(input("VALOR DO SAQUE: R$ "))

            if valor_saque > 0:

                if dados_cliente[4] >= valor_saque:
                    saldo_saque = dados_cliente[4] - valor_saque
                    dados_cliente[4] = saldo_saque
                    mensagem = "SAQUE REALIZADO COM SUCESSO!"

                elif (dados_cliente[4] + dados_cliente[5]) >= valor_saque: 
                    saldo_saque = (dados_cliente[4] + dados_cliente[5]) - valor_saque
                    dados_cliente[4] = 0
                    dados_cliente[5] = saldo_saque
                    print("VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO.")
                    mensagem = "SAQUE REALIZADO COM SUCESSO!"
                
                else:
                    mensagem = "SALDO INSUFICIENTE."
            else:
                mensagem = "VALOR INVÁLIDO!"
        else:
            mensagem = "SENHA INVÁLIDA!"
            tentativa_senha =+ 1
    else: 
        mensagem = "NÚMERO DA CONTA INVÁLIDO!"


    if mensagem != "SAQUE REALIZADO COM SUCESSO!":
        input(f"{mensagem} Pressione ENTER para tentar novamente...")
        saque(dados_cliente, saques_depositos)
    
    elif tentativa_senha > 3:
        bloqueado = True
        menu()
    else:
        input(f"{mensagem} Pressione ENTER para prosseguir.")
        menu()

    valor_saque = -valor_saque
    saques_depositos.append(valor_saque)

    return dados_cliente, saques_depositos

def consulta_saldo(dados_cliente):

    limpar_tela()

    print("MACK BANK – CONSULTA SALDO")

    numero_conta = int(input("INFORME O NÚMERO DA CONTA: "))

    if (numero_conta == dados_cliente[0]):
        print(f"NOME DO CLIENTE: {dados_cliente[1]}")

        senha = input("INFORME A SENHA: ")

        if senha == dados_cliente[6]:
            tentativa_senha = 1
            print(f"SALDO EM CONTA: R$ {dados_cliente[4]}")
            print(f"LIMITE DE CRÉDITO: R$ {dados_cliente[5]}")
            mensagem = "Volte ao menu."
        else:
            mensagem = "SENHA INVÁLIDA!"
            tentativa_senha =+ 1
    else:
        mensagem = "NÚMERO DA CONTA INVÁLIDO!"

    if tentativa_senha > 3:
        bloqueado = True
        menu()
        
    if mensagem != "SENHA INVÁLIDA!" or mensagem != "NÚMERO DA CONTA INVÁLIDO!":
        input(f"{mensagem} Pressione ENTER para prosseguir.")

    return dados_cliente

def consultar_extrato(dados_cliente, saques_depositos):

    limpar_tela()

    print("MACK BANK – EXTRATO DA CONTA")

    numero_conta = int(input("INFORME O NÚMERO DA CONTA: "))

    if (numero_conta == dados_cliente[0]):
        print(f"NOME DO CLIENTE: {dados_cliente[1]}")

        senha = input("INFORME A SENHA: ")

        if senha == dados_cliente[6]:
            print(f"LIMITE DE CRÉDITO: R$ {dados_cliente[5]}")


            for i in range(len(saques_depositos)):
                if saques_depositos[i] < 0:
                    print(f"SAQUE: {saques_depositos[i]}")
                else:
                    print(f"DEPOSITO: {saques_depositos[i]}")

            print(f"SALDO EM CONTA: R$ {dados_cliente[4]}")

            input("Presione ENTER para voltar ao menu inicial.")
    
    else:
        input("NÚMERO DA CONTA INVÁLIDO! Pressione ENTER para tentar novamente...")
        consultar_extrato()

    return dados_cliente, saques_depositos

        
fim = False
cadastro_preenchido = False
bloqueado = False
saques_depositos = []
dados_cliente = []

while not fim:

    limpar_tela()
    menu()

    opcao = int(input("Sua opção: "))

    match opcao:
        
        # cadastro
        case 1:
            if not cadastro_preenchido:
                limpar_tela()
                dados_cliente = cadastro_cliente(dados_cliente)
                cadastro_preenchido = True
            else:
                input("O cadastro já foi feito. Presione ENTER para voltar ao menu inicial.")
        # deposito
        case 2:
            if not bloqueado:
                if not cadastro_preenchido:
                    limpar_tela()
                    input("O cadastro ainda não foi feito. Presione ENTER para voltar ao menu inicial.")
                else:
                    dados_cliente, saques_depositos = deposito(dados_cliente, saques_depositos)
            else:
                input("Conta bloqueada. Presione ENTER para voltar ao menu inicial.")
        # saque
        case 3:
            if not bloqueado:
                if not cadastro_preenchido:
                    limpar_tela()
                    input("O cadastro ainda não foi feito. Presione ENTER para voltar ao menu inicial.")
                else:
                    dados_cliente, saques_depositos = saque(dados_cliente, saques_depositos)
            else:
                input("Conta bloqueada. Presione ENTER para voltar ao menu inicial.")
         
        # consulta saldo
        case 4:
            if not bloqueado:
                if not cadastro_preenchido:
                    limpar_tela()
                    input("O cadastro ainda não foi feito. Presione ENTER para voltar ao menu inicial.")
                else:
                    dados_cliente = consulta_saldo(dados_cliente)
            else:
                input("Conta bloqueada. Presione ENTER para voltar ao menu inicial.")

        # consulta extrato
        case 5:
            if not bloqueado:
                if not cadastro_preenchido:
                    limpar_tela()
                    input("O cadastro ainda não foi feito. Presione ENTER para voltar ao menu inicial.")
                else:
                    dados_cliente, saques_depositos = consultar_extrato(dados_cliente, saques_depositos)
            else:
                input("Conta bloqueada. Presione ENTER para voltar ao menu inicial.")
        # finalizar
        case 6:
            fim = True
        # opção inválida
        case _:
            print("\nDigite uma opção válida! Pressine alguma tecla para voltar ao menu...")
            msvcrt.getch()

limpar_tela()
print("""MACK BANK – SOBRE
      
Este programa foi desenvolvido por:

Arthur Santana - 32391854
Daniel Monteiro - 32389574
""")