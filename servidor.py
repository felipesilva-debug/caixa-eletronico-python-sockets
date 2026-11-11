servidor.py

from socket import *

# Configuração da conexão
HOST = '127.0.0.1'
PORTA = 5000

# Saldo inicial
saldo = 0.0

# Matrícula e senha válidas
MATRICULA = "123456"
SENHA = "12345"

# Cria o socket
sockobj = socket(AF_INET, SOCK_STREAM)

# Associa o socket ao IP e à porta
sockobj.bind((HOST, PORTA))

# Coloca o servidor para escutar conexões
sockobj.listen(1)

print("Servidor iniciado...")
print(f"Aguardando conexão na porta {PORTA}...")

while True:

    # Aceita a conexão do cliente
    conexao, endereco = sockobj.accept()

    print(f"\nCliente conectado: {endereco}")

    # -------------------------
    # LOGIN
    # -------------------------

    while True:

        # Recebe a matrícula
        matricula = conexao.recv(1024).decode()

        # Recebe a senha
        senha = conexao.recv(1024).decode()

        # Verifica as credenciais
        if matricula == MATRICULA and senha == SENHA:
            conexao.send("Login realizado com sucesso!".encode())
            break
        else:
            conexao.send("Falha no login. Matrícula ou senha incorreta.".encode())

    # -------------------------
    # MENU DO CAIXA
    # -------------------------

    while True:

        # Recebe a opção escolhida pelo cliente
        opcao = conexao.recv(1024).decode()

        # -------------------------
        # DEPOSITAR
        # -------------------------

        if opcao == "1":

            valor = float(conexao.recv(1024).decode())

            saldo += valor

            resposta = f"Depósito realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}"

            conexao.send(resposta.encode())

        # -------------------------
        # SACAR
        # -------------------------

        elif opcao == "2":

            valor = float(conexao.recv(1024).decode())

            if valor > saldo:

                resposta = "Saldo insuficiente."

            else:

                saldo -= valor

                resposta = f"Saque realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}"

            conexao.send(resposta.encode())

        # -------------------------
        # VISUALIZAR SALDO
        # -------------------------

        elif opcao == "3":

            resposta = f"Saldo atual: R$ {saldo:.2f}"

            conexao.send(resposta.encode())

        # -------------------------
        # SAIR
        # -------------------------

        elif opcao == "4":

            conexao.send("Conexão encerrada. Até logo!".encode())

            print(f"Cliente desconectado: {endereco}")

            conexao.close()

            break

        # -------------------------
        # OPÇÃO INVÁLIDA
        # -------------------------

        else:

            conexao.send("Opção inválida.".encode())