menu = """
Selecione a opção desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    # Exibe o menu e recebe a opção do usuário
    opcao = input(menu) 

    if opcao == "1":
        deposito = float(input("Informe o valor do depósito:"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Valor de depósito inválido. Tente novamente.")

    elif opcao == "2":
        saque = float(input("Informe o valor para saque:"))
        if saque > saldo:
            print("Saldo insuficiente para saque.")
        elif saque > limite:
            print(f"Saque acima do limite de R$ {limite:.2f}. Tente outro valor")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saques diários atingido ({LIMITE_SAQUES}). Tente novamente amanhã")
        else:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {saque:.2f} realizado com sucesso. Retire o dinheiro.")
            
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Nenhuma transação realizada.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==========================================\n")
    
    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, selecione uma das opções do menu.")
