cliente.py

from socket import *

# Configuração da conexão
HOST = '127.0.0.1'
PORTA = 5000

# Cria o socket
conexao = socket(AF_INET, SOCK_STREAM)

# Conecta ao servidor
conexao.connect((HOST, PORTA))

print("Conectado ao servidor!")
print()

# -------------------------
# LOGIN
# -------------------------

while True:

    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")

    # Envia matrícula
    conexao.send(matricula.encode())

    # Envia senha
    conexao.send(senha.encode())

    # Recebe resposta do servidor
    resposta = conexao.recv(1024).decode()

    print(resposta)
    print()

    # Se o login estiver correto, continua
    if resposta == "Login realizado com sucesso!":
        break

# -------------------------
# MENU
# -------------------------

while True:

    print("====== CAIXA ELETRÔNICO ======")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Visualizar Saldo")
    print("4 - Sair")
    print("==============================")

    opcao = input("Escolha uma opção: ")

    # Envia a opção para o servidor
    conexao.send(opcao.encode())

    # -------------------------
    # DEPOSITAR
    # -------------------------

    if opcao == "1":

        valor = input("Digite o valor para depósito: ")

        conexao.send(valor.encode())

        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)
        print()

    # -------------------------
    # SACAR
    # -------------------------

    elif opcao == "2":

        valor = input("Digite o valor para saque: ")

        conexao.send(valor.encode())

        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)
        print()

    # -------------------------
    # SALDO
    # -------------------------

    elif opcao == "3":

        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)
        print()

    # -------------------------
    # SAIR
    # -------------------------

    elif opcao == "4":

        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)

        conexao.close()

        break

    # -------------------------
    # OPÇÃO INVÁLIDA
    # -------------------------

    else:

        resposta = conexao.recv(1024).decode()

        print()
        print(resposta)
        print()