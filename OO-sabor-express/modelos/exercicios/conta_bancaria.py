class ContaBancaria:
    contasBancarias = []
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contasBancarias.append(self)

    def __str__(self):
        return f'{self._titular} | {self._saldo} | {self._ativo}'
    
    def ativar_conta(self):
        self._ativo = not self._ativo
    


conta1 = ContaBancaria('Chiquinho', '1.000.000.00')
conta2 = ContaBancaria('Narcisa', '1.089.558.00')

print(conta1)
print(conta2)

conta1.ativar_conta()
print(conta1)