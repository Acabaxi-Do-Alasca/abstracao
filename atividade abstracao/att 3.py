class ContaBancaria:
    def __init__(self, titular, numero):
        self.titular = titular
        self.saldo = 0  # Saldo inicial é 0
        self.numero = numero

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor de saque inválido.')

    def exibir_saldo(self):
        print(f'Saldo da conta de {self.titular}: R${self.saldo:.2f}')


# Criar duas contas bancárias
conta1 = ContaBancaria("João", "12345")
conta2 = ContaBancaria("Maria", "67890")

# Realizar operações de depósito e saque
conta1.depositar(1000)
conta1.sacar(500)
conta1.exibir_saldo()

conta2.depositar(500)
conta2.sacar(1000)
conta2.exibir_saldo()
