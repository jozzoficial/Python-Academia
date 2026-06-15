class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular  # Atributo público
        self._saldo = saldo_inicial  # Atributo protegido (convenção)
        self.__numero_conta = "12345"  # Atributo privado (name mangling)

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(
                f"Depósito de {valor} Kz. "
                f"Novo saldo: {self._saldo} Kz."
            )
        else:
            print("Valor de depósito inválido.")

    def levantar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(
                f"Levantamento de {valor} Kz. "
                f"Novo saldo: {self._saldo} Kz."
            )
        else:
            print(
                "Saldo insuficiente ou valor de levantamento inválido."
            )

    def get_saldo(self):
        return self._saldo


# Exemplo de uso
minha_conta = ContaBancaria("João", 1000)

print(f"Titular: {minha_conta.titular}")
print(f"Saldo (via método): {minha_conta.get_saldo()} Kz.")

minha_conta.depositar(500)
minha_conta.levantar(200)

# Acesso direto (desencorajado para _saldo e mais difícil para __numero_conta)

# print(minha_conta._saldo)
# Funciona, mas é má prática

# print(minha_conta.__numero_conta)
# Erro: AttributeError

# print(minha_conta._ContaBancaria__numero_conta)
# Funciona (name mangling)