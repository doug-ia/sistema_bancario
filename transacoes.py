from datetime import datetime

class Conta:
    def __init__(self):
        self.transacoes = []
        self.limites_diarios = 10

    def realizar_transacao(self, valor):
        hoje = datetime.now()
        transacao_hoje = [t for t in self.transacoes if t[0].date() == hoje]

        if len(self.transacoes) >= self.limites_diarios:
            print("Limite Diarios de Transações Atingidos!")

        else:
            agora = datetime.now()
            self.transacoes.append((agora, valor))
            print(f'Transação de R$ {valor:.2f} realizada com sucesso!')

    def extrato(self):
        print('Extrato de Transações:')
        for data, valor in self.transacoes:
            print(f'Data: {data.strftime('%d/%m/%Y %H:%M:%S')} | Valor: {valor:.2f}')


conta = Conta()

while True:
    print("\n1. Realizar Transações")
    print("2. Verificar Extrato")
    print("3. Sair")

    opcao = input("Escolha uma Opção: ")
    if opcao == "1":
        valor = float(input('Informe o Valor da Transação: R$'))
        conta.realizar_transacao(valor)

    elif opcao == "2":
        conta.extrato()

    elif opcao == "3":
        break

    else:
        print("Opção Invalida, Tente Novamente")

