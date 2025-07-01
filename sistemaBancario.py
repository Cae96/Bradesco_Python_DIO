import os
import time

saldo = 1000
limite = 500
saques_diarios = 3
extrato = ""
listaCPF = []
listaContas = []
usuarios = {}
AGENCIA = "0001"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def sacar(*, saldo, saques_diarios, extrato):
    if saques_diarios > 0:
        while True:
            try:
                saque = int(input("Quanto deseja sacar? "))
                break
            except:
                print("O valor deve ser um número inteiro positivo.")

        if saque > 500 or saque <= 0:
            print("Valor inválido, limite por saque: 500 reais")
        else:
            if saque <= saldo:
                saldo -= saque
                print("Saque efetuado com sucesso, favor retirar seu dinheiro")
                extrato += f"Saque: R$ {saque:.2f}\n"
                saques_diarios -= 1
            else:
                print(f"Saldo insuficiente, seu saldo é de: R$ {saldo:.2f}")
    else:
        print("Você esgotou seu limite de saques diários")
        print("Retornando ao MENU principal...")

    return saldo, saques_diarios, extrato

def depositar(saldo, extrato, /):
    while True:
        try:
            deposito = float(input("Quanto deseja depositar? "))
            if deposito > 0:
                saldo += deposito
                print("Depósito efetuado com sucesso!")
                extrato += f"Depósito: R$ {deposito:.2f}\n"
                break
            else:
                print("Valor inválido, deve ser maior que 0")
        except:
            print("O valor deve ser um número positivo")

    return saldo, extrato

def extrato_funcao(saldo, extrato):
    clear_terminal()
    print("-----------EXTRATO-----------")
    print(extrato if extrato else "Nenhuma movimentação registrada.")
    print(f"Seu saldo é de R$ {saldo:.2f}")
    print("------------------------------")

def validar_CPF():
    while True:
        CPF = input("Digite o CPF: ")
        try:
            int(CPF)
        except:
            print("Formato de CPF inválido, deve conter somente números e 11 dígitos")
            continue

        if len(CPF) == 11 and int(CPF) >= 0:
            if CPF in listaCPF:
                print("CPF já cadastrado")
            else:
                listaCPF.append(CPF)
                return CPF
        else:
            print("Verifique a quantidade de dígitos")

def criar_usuario():
    clear_terminal()
    print("----------CRIAR USUÁRIO---------\n")
    cpf = validar_CPF()
    nome = input("Qual seu nome completo: ")
    endereco = input("Qual seu endereço: ")
    usuarios[cpf] = {
        "nome": nome,
        "endereco": endereco,
        "agência": AGENCIA,
        "contas": []
    }

def criar_conta():
    cpf = input("Qual o CPF do cliente? ")
    if cpf in usuarios:
        numero_conta = f"{len(listaContas)+1:04d}"  # Ex: 0001, 0002...
        listaContas.append(numero_conta)
        usuarios[cpf]["contas"].append(numero_conta)
        print(f"Conta criada com sucesso. Número da conta: {numero_conta}")
    else:
        print("CPF não encontrado, favor cadastrar o cliente primeiro")

# Função principal
while True:
    clear_terminal()
    print("""
    ----------MENU----------

    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Criar Usuário
    5 - Listar Usuários
    6 - Criar Conta
    0 - Sair

    ------------------------""")

    operacao = input("Digite a operação que deseja fazer: ")

    if operacao == "0":
        print("Sistema finalizado!")
        break

    elif operacao == "1":
        saldo, saques_diarios, extrato = sacar(saldo=saldo, saques_diarios=saques_diarios, extrato=extrato)
        time.sleep(2)

    elif operacao == "2":
        saldo, extrato = depositar(saldo, extrato)
        time.sleep(2)

    elif operacao == "3":
        extrato_funcao(saldo, extrato)
        input("Pressione qualquer tecla para voltar ao MENU")

    elif operacao == "4":
        criar_usuario()
        input("Pressione qualquer tecla para voltar ao MENU")

    elif operacao == "5":
        print("--------LISTA DE USUÁRIOS--------\n")
        for cpf, dados in usuarios.items():
            contas = ', '.join(dados['contas']) if dados['contas'] else 'Nenhuma conta'
            print(f"CPF: {cpf} | Nome: {dados['nome']} | Endereço: {dados['endereco']}| Agência:{AGENCIA} | Contas: {contas}")
        input("\nPressione qualquer tecla para voltar ao MENU")

    elif operacao == "6":
        criar_conta()
        input("Pressione qualquer tecla para voltar ao MENU")