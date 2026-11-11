README.md

# Sistema de Caixa Eletrônico

Projeto acadêmico desenvolvido em Python utilizando a biblioteca `socket` para estabelecer uma comunicação entre um programa **Cliente** e um **Servidor**.



## Objetivo

O objetivo do projeto é desenvolver um sistema simples de caixa eletrônico, dividido em dois ambientes:

* **Cliente:** responsável pela interação com o usuário.
* **Servidor:** responsável por receber, processar e responder às solicitações do cliente.

O sistema possui as seguintes operações:

1. Depositar
2. Sacar
3. Visualizar Saldo
4. Sair

Além disso, antes de utilizar o sistema, o usuário precisa realizar um login através de sua matrícula e senha.



##  Estrutura do projeto

```text
caixa_eletronico/
│
├── cliente.py
├── servidor.py
└── README.md
```

### `cliente.py`

Responsável por:

* Conectar-se ao servidor;
* Solicitar matrícula e senha;
* Enviar os dados de autenticação;
* Exibir o menu do caixa eletrônico;
* Enviar as operações escolhidas;
* Exibir as respostas recebidas do servidor.

### `servidor.py`

Responsável por:

* Criar e disponibilizar o servidor;
* Aceitar a conexão do cliente;
* Validar matrícula e senha;
* Armazenar o saldo;
* Processar depósitos;
* Processar saques;
* Consultar o saldo;
* Enviar as respostas ao cliente.



#  Comunicação Cliente x Servidor

A comunicação é realizada utilizando a biblioteca `socket` do Python.

O projeto utiliza:

* **IPv4**
* **TCP**
* **IP:** `127.0.0.1`
* **Porta:** `5000`

O endereço `127.0.0.1` representa o próprio computador, portanto o cliente e o servidor podem ser executados na mesma máquina.

A comunicação ocorre basicamente da seguinte maneira:

```text
┌──────────────┐
│    CLIENTE   │
│ cliente.py   │
└──────┬───────┘
       │
       │  Socket / TCP
       │
       ▼
┌──────────────┐
│   SERVIDOR   │
│ servidor.py  │
└──────┬───────┘
       │
       │ Processamento
       ▼
┌──────────────┐
│    RESPOSTA  │
└──────┬───────┘
       │
       ▼
    CLIENTE
```



# Login

Antes de acessar o caixa eletrônico, o usuário precisa informar:

```text
Matrícula: 123456
Senha: 12345
```

Esses dados são enviados pelo `cliente.py` para o `servidor.py`.

O servidor compara os dados recebidos com as credenciais cadastradas.

Caso estejam corretos:

```text
Login realizado com sucesso!
```

Caso estejam incorretos:

```text
Falha no login. Matrícula ou senha incorreta.
```

O usuário poderá tentar novamente.



#  Operações

## 1. Depositar

O usuário informa o valor que deseja depositar.

Exemplo:

```text
Escolha uma opção: 1
Digite o valor para depósito: 500
```

O cliente envia o valor ao servidor.

O servidor adiciona o valor ao saldo:

```python
saldo += valor
```

Depois, envia o novo saldo para o cliente.

Exemplo:

```text
Depósito realizado com sucesso!
Saldo atual: R$ 500.00
```



## 2. Sacar

O usuário informa o valor que deseja sacar.

Exemplo:

```text
Escolha uma opção: 2
Digite o valor para saque: 100
```

O servidor verifica se existe saldo suficiente.

Se o valor for maior que o saldo:

```text
Saldo insuficiente.
```

Caso contrário, o valor é retirado:

```python
saldo -= valor
```

E o novo saldo é enviado ao cliente.



## 3. Visualizar Saldo

Ao selecionar:

```text
3 - Visualizar Saldo
```

O cliente solicita o saldo atual ao servidor.

O servidor consulta a variável:

```python
saldo
```

E envia o resultado para o cliente.

Exemplo:

```text
Saldo atual: R$ 400.00
```



## 4. Sair

Ao selecionar:

```text
4 - Sair
```

O servidor envia uma mensagem de encerramento e a conexão é fechada.

```python
conexao.close()
```



# Principais funções do Socket

## `socket()`

Cria o socket utilizado para a comunicação.

```python
socket(AF_INET, SOCK_STREAM)
```

### `AF_INET`

Indica a utilização do protocolo IPv4.

### `SOCK_STREAM`

Indica a utilização do protocolo TCP.



## `bind()`

Utilizado pelo servidor para associar o socket a um endereço IP e uma porta.

```python
sockobj.bind((HOST, PORTA))
```



## `listen()`

Coloca o servidor em estado de espera por conexões.

```python
sockobj.listen(1)
```



## `accept()`

Aceita uma conexão recebida pelo servidor.

```python
conexao, endereco = sockobj.accept()
```



## `connect()`

Utilizado pelo cliente para estabelecer uma conexão com o servidor.

```python
conexao.connect((HOST, PORTA))
```



## `send()`

Utilizado para enviar dados através do socket.

```python
conexao.send(mensagem.encode())
```

Como o socket trabalha com bytes, o texto é convertido utilizando:

```python
.encode()
```



## `recv()`

Utilizado para receber dados.

```python
dados = conexao.recv(1024)
```

Depois, os dados podem ser convertidos novamente para texto:

```python
dados.decode()
```



#  Fluxo de comunicação

Um exemplo de comunicação durante um depósito:

```text
CLIENTE                         SERVIDOR
   │                               │
   │─────── "1" ─────────────────►│
   │                               │
   │─────── "500" ───────────────►│
   │                               │
   │                         saldo += 500
   │                               │
   │◄── "Saldo: R$ 500.00" ───────│
   │                               │
```

O fluxo geral é:

```text
Usuário
   ↓
cliente.py
   ↓
send()
   ↓
servidor.py
   ↓
recv()
   ↓
Processamento
   ↓
send()
   ↓
cliente.py
   ↓
recv()
   ↓
Usuário
```



#  Como executar o projeto

## 1. Abrir o projeto

Abra a pasta `caixa_eletronico` no Visual Studio Code.

A estrutura deve ser:

```text
C:\felipe\vscode\caixa_eletronico\
│
├── cliente.py
├── servidor.py
└── README.md
```



## 2. Abrir o terminal

No VS Code:

```text
Terminal → New Terminal
```

O terminal deve estar dentro da pasta do projeto:

```text
PS C:\felipe\vscode\caixa_eletronico>
```



## 3. Iniciar o servidor

Execute:

```powershell
py servidor.py
```

Se o comando `py` não funcionar, pode ser utilizado:

```powershell
python servidor.py
```

O resultado esperado é:

```text
Servidor iniciado...
Aguardando conexão na porta 5000...
```

**Não feche esse terminal.**



## 4. Iniciar o cliente

Abra um segundo terminal no VS Code.

Execute:

```powershell
py cliente.py
```

O resultado esperado:

```text
Conectado ao servidor!

Digite sua matrícula:
```



#  Credenciais para teste

Para a versão atual do projeto:

```text
Matrícula: 123456
Senha: 12345
```

Essas informações estão definidas no arquivo `servidor.py`.



#  Exemplo de utilização

### Login

```text
Digite sua matrícula: 123456
Digite sua senha: 12345

Login realizado com sucesso!
```

### Menu

```text
====== CAIXA ELETRÔNICO ======
1 - Depositar
2 - Sacar
3 - Visualizar Saldo
4 - Sair
==============================
```

### Depósito

```text
Escolha uma opção: 1
Digite o valor para depósito: 500

Depósito realizado com sucesso!
Saldo atual: R$ 500.00
```

### Saque

```text
Escolha uma opção: 2
Digite o valor para saque: 200

Saque realizado com sucesso!
Saldo atual: R$ 300.00
```

### Consulta

```text
Escolha uma opção: 3

Saldo atual: R$ 300.00
```

### Encerramento

```text
Escolha uma opção: 4

Conexão encerrada. Até logo!
```



#  Tecnologias utilizadas

* **Python 3**
* **Biblioteca Socket**
* **Protocolo TCP**
* **IPv4**
* **Visual Studio Code**



#  Conceitos trabalhados

O projeto permite praticar conceitos de:

* Programação em Python;
* Comunicação cliente-servidor;
* Sockets;
* TCP/IP;
* Endereçamento IP;
* Portas de comunicação;
* Envio e recebimento de dados;
* `encode()` e `decode()`;
* Estruturas condicionais;
* Loops;
* Variáveis;
* Entrada e saída de dados;
* Autenticação básica;
* Processamento de operações.



#  Observações

Este projeto possui finalidade acadêmica e didática.

A autenticação utiliza valores definidos diretamente no código e não possui mecanismos de segurança adequados para um sistema bancário real.

O saldo também é mantido apenas durante a execução do servidor. Ao encerrar o programa, o valor armazenado na variável `saldo` é perdido.



#  Projeto acadêmico

**Projeto:** Sistema de Caixa Eletrônico
**Linguagem:** Python
**Comunicação:** Socket TCP
**Ambiente:** Cliente x Servidor

