saldo = 0
saques_realizados = 0
limite_saques = 3
limite_valor_saque = 500
depositos = []
saques = []

# Realiza os Depositos
def realizar_deposito():
    global saldo
    try:
        valor = float(input("Digite o valor de depósito (VALORES ACIMA DE 0): "))
        if valor > 0:
            saldo += valor
            depositos.append(valor)
            print(f"Valor depositado! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Erro: O valor do depósito deve ser positivo.")
    except ValueError:
        print("Erro: Por favor, digite um valor válido.")


# Realiza os Saques
def realizar_saque():
    global saldo, saques_realizados
    if saques_realizados >= limite_saques:
        print("Erro: Limite de 3 saques diários atingido.")
        return
    
    try:
        valor = float(input("Digite o valor de saque: "))
        
        if valor <= 0:
            print("Erro: O valor de saque deve ser positivo!")
        elif valor > saldo:
            print(f"Erro: Saldo insuficiente - Seu saldo atual é: R$ {saldo:.2f}")
        elif valor > limite_valor_saque:
            print(f"Erro: O valor máximo para saque é R$ {limite_valor_saque:.2f}.")
        else:
            saques_realizados += 1
            saldo -= valor
            saques.append(valor)
            print(f"Saque realizado com sucesso! - Seu saldo atual é: R$ {saldo:.2f}")
    except ValueError:
        print("Erro: Por favor, digite um valor válido.")

# Reseta o Limite do Saque do Cliente
def resetar_limite_saques():
    global saques_realizados
    saques_realizados = 0
    print("Seus saques foram resetados.")

# Visualiza o extrato
def realizar_extrato():
    global depositos, saques
    print("------------ EXTRATO ------------")
    
    if not depositos and not saques:
        print('Não há operações realizadas ainda.')

    else:

        print('Depositos Realizados:')
        if depositos:
            for i, deposito in enumerate(depositos, 1):
                print(f'Deposito {i}: R$ {deposito:.2f}')

        else:
            print("Nenhum Deposito Realizado.")

        print('Saques Realizados:')
        if saques:
            for i, saque in enumerate(saques, 1):
                print(f'Saques {i}: R$ {saque:.2f}')

        else:
            print("Nenhum Saque Realizado")

    print(f'\nSaldo Atual: R$ {saldo:.2f}')


while True:
    print("\n---------- Menu -----------")
    print("1 - Para realizar DEPÓSITO")
    print("2 - Para realizar SAQUE")
    print("3 - Para resetar limite de saques")
    print("4 - Para Visualizar o EXTRATO")
    print("5 - Para sair")
    
    # Garantir que a entrada do usuário não tenha espaços extras
    opcao = input("Escolha uma opção: ").strip()

    # Verificações
    if opcao == '1':
        realizar_deposito()
    elif opcao == '2':
        realizar_saque()
    elif opcao == '3':
        resetar_limite_saques()
    elif opcao == '4':
        realizar_extrato()
    elif opcao == '5':
        print("Saindo do sistema. Obrigado, volte sempre!")
        break
    else:
        print("Opção inválida, tente novamente.")
