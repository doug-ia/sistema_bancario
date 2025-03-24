saldo = 0
saques_realizados = 0
limite_saques = 3
limite_valor_saque = 500
depositos = []
saques = []
usuarios = []  # Lista para armazenar usuários e contas

# Função para criar usuário
def criar_usuario():
    global usuarios
    nome = input("Digite o nome completo do usuário: ").strip()
    cpf = input("Digite o CPF do usuário (somente números): ").strip()
    
    # Verificando se o CPF já está cadastrado
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Erro: CPF já cadastrado!")
    else:
        usuario = {'nome': nome, 'cpf': cpf, 'conta_corrente': None}
        usuarios.append(usuario)
        print(f"Usuário {nome} criado com sucesso!")

# Função para criar uma conta corrente vinculada a um usuário
def criar_conta_corrente():
    global usuarios
    cpf = input("Digite o CPF do usuário para vincular à conta: ").strip()

    # Buscando o usuário pelo CPF
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    
    if usuario:
        if usuario['conta_corrente']:
            print("Erro: Este usuário já possui uma conta corrente vinculada!")
        else:
            # Criação de uma conta corrente com saldo, depósitos e saques
            usuario['conta_corrente'] = {'saldo': 0, 'saques_realizados': 0, 'depositos': [], 'saques': []}
            print(f"Conta corrente criada com sucesso para {usuario['nome']}.")
    else:
        print("Erro: Usuário não encontrado.")

# Função para buscar e verificar a conta do usuário, para realizar depositos
def verificar_conta(cpf):
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario and usuario['conta_corrente']:
        return usuario['conta_corrente']
    else:
        print("Erro: Usuário ou conta corrente não encontrado.")
        return None

# Realiza os Depósitos
def realizar_deposito():
    cpf = input("Digite o CPF do usuário para realizar o depósito: ").strip()
    conta_corrente = verificar_conta(cpf)
    
    if conta_corrente:
        try:
            valor = float(input("Digite o valor de depósito (VALORES ACIMA DE 0): "))
            if valor > 0:
                conta_corrente['saldo'] += valor
                conta_corrente['depositos'].append(valor)
                print(f"Valor depositado! Saldo atual: R$ {conta_corrente['saldo']:.2f}")
            else:
                print("Erro: O valor do depósito deve ser positivo.")
        except ValueError:
            print("Erro: Por favor, digite um valor válido.")

# Realiza os Saques
def realizar_saque():
    cpf = input("Digite o CPF do usuário para realizar o saque: ").strip()
    conta_corrente = verificar_conta(cpf)
    
    if conta_corrente:
        if conta_corrente['saques_realizados'] >= limite_saques:
            print("Erro: Limite de 3 saques diários atingido.")
            return
        
        try:
            valor = float(input("Digite o valor de saque: "))
            if valor <= 0:
                print("Erro: O valor de saque deve ser positivo!")
            elif valor > conta_corrente['saldo']:
                print(f"Erro: Saldo insuficiente - Seu saldo atual é: R$ {conta_corrente['saldo']:.2f}")
            elif valor > limite_valor_saque:
                print(f"Erro: O valor máximo para saque é R$ {limite_valor_saque:.2f}.")
            else:
                conta_corrente['saques_realizados'] += 1
                conta_corrente['saldo'] -= valor
                conta_corrente['saques'].append(valor)
                print(f"Saque realizado com sucesso! - Seu saldo atual é: R$ {conta_corrente['saldo']:.2f}")
        except ValueError:
            print("Erro: Por favor, digite um valor válido.")

# Reseta o Limite de Saques
def resetar_limite_saques():
    cpf = input("Digite o CPF do usuário para resetar o limite de saques: ").strip()
    conta_corrente = verificar_conta(cpf)
    
    if conta_corrente:
        conta_corrente['saques_realizados'] = 0
        print("Limite de saques resetado.")
    else:
        print("Erro: Conta não encontrada.")

# Visualiza o Extrato
def realizar_extrato():
    cpf = input("Digite o CPF do usuário para visualizar o extrato: ").strip()
    conta_corrente = verificar_conta(cpf)
    
    if conta_corrente:
        print("------------ EXTRATO ------------")
        print(f"Depositos Realizados: {len(conta_corrente['depositos'])}")
        for i, deposito in enumerate(conta_corrente['depositos'], 1):
            print(f"Deposito {i}: R$ {deposito:.2f}")
        
        print(f"Saques Realizados: {len(conta_corrente['saques'])}")
        for i, saque in enumerate(conta_corrente['saques'], 1):
            print(f"Saque {i}: R$ {saque:.2f}")
        
        print(f"\nSaldo Atual: R$ {conta_corrente['saldo']:.2f}")
    else:
        print("Erro: Conta não encontrada.")

# Menu principal
while True:
    print("\n---------- Menu -----------")
    print("1 - Para criar um USUÁRIO")
    print("2 - Para criar uma CONTA CORRENTE")
    print("3 - Para realizar DEPÓSITO")
    print("4 - Para realizar SAQUE")
    print("5 - Para resetar limite de saques")
    print("6 - Para Visualizar o EXTRATO")
    print("7 - Para sair")
    
    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        criar_usuario()
    elif opcao == '2':
        criar_conta_corrente()
    elif opcao == '3':
        realizar_deposito()
    elif opcao == '4':
        realizar_saque()
    elif opcao == '5':
        resetar_limite_saques()
    elif opcao == '6':
        realizar_extrato()
    elif opcao == '7':
        print("Saindo do sistema. Obrigado, volte sempre!")
        break
    else:
        print("Opção inválida, tente novamente.")
