def formatar_reais(valor):
    """Transforma 1234.50 em R$ 1.234,50."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


class ContaBancaria:
    def __init__(self, numero, titular, cpf, agencia, tipo):
        self.numero = numero
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.tipo = tipo
        self.saldo = 0.0
        self.situacao = "Ativa"

    def apresentarDados(self):
        print("\n========== BANCO HORIZONTE ==========")
        print(f"Conta: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Agência: {self.agencia}")
        print(f"Tipo: {self.tipo}")
        print(f"Saldo: {formatar_reais(self.saldo)}")
        print(f"Situação: {self.situacao}")
        print("=====================================")

    def depositar(self, valor):
        if self.situacao == "Bloqueada":
            print("Depósito recusado: a conta está bloqueada.")
            return False
        if valor <= 0:
            print("Depósito recusado: o valor deve ser maior que zero.")
            return False

        self.saldo += valor
        print(f"Depósito de {formatar_reais(valor)} realizado com sucesso!")
        return True

    def sacar(self, valor):
        if self.situacao == "Bloqueada":
            print("Saque recusado: a conta está bloqueada.")
            return False
        if valor <= 0:
            print("Saque recusado: o valor deve ser maior que zero.")
            return False
        if valor > self.saldo:
            print("Saque recusado: saldo insuficiente.")
            return False

        self.saldo -= valor
        print(f"Saque de {formatar_reais(valor)} realizado com sucesso!")
        return True

    def consultarSaldo(self):
        print(f"Saldo da conta {self.numero}: {formatar_reais(self.saldo)}")
        return self.saldo

    def alterarTitular(self, novo_nome):
        if not novo_nome.strip():
            print("Alteração recusada: o nome não pode estar vazio.")
            return False

        self.titular = novo_nome.strip()
        print(f"Titular alterado com sucesso para: {self.titular}")
        return True

    def bloquearConta(self):
        if self.situacao == "Bloqueada":
            print("A conta já está bloqueada.")
            return False

        self.situacao = "Bloqueada"
        print(f"Conta {self.numero} bloqueada com sucesso.")
        return True

    def desbloquearConta(self):
        if self.situacao == "Ativa":
            print("A conta já está ativa.")
            return False

        self.situacao = "Ativa"
        print(f"Conta {self.numero} desbloqueada com sucesso.")
        return True

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("Transferência recusada: o valor deve ser maior que zero.")
            return False
        if self.situacao == "Bloqueada":
            print("Transferência recusada: conta de origem bloqueada.")
            return False
        if conta_destino.situacao == "Bloqueada":
            print("Transferência recusada: conta de destino bloqueada.")
            return False
        if valor > self.saldo:
            print("Transferência recusada: saldo insuficiente.")
            return False
        if self is conta_destino:
            print("Transferência recusada: origem e destino são a mesma conta.")
            return False

        # Os saldos só mudam depois de todas as validações.
        self.saldo -= valor
        conta_destino.saldo += valor
        print(
            f"Transferência de {formatar_reais(valor)} realizada com sucesso! "
            f"Conta {self.numero} -> Conta {conta_destino.numero}"
        )
        return True

    def emitirRelatorio(self):
        print("\n========== RELATÓRIO DA CONTA ==========")
        print(f"Número da conta: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Agência: {self.agencia}")
        print(f"Tipo da conta: {self.tipo}")
        print(f"Saldo disponível: {formatar_reais(self.saldo)}")
        print(f"Situação atual: {self.situacao}")
        print("=======================================")



""" AREA DE TESTES DO CODIGO """


# teste 1 (criar 3 contas)

print("\nTESTE 1 - Criando as contas bancárias")

ana = ContaBancaria("1001", "Ana Souza", "123.456.789-00", "Centro", "Corrente")
carlos = ContaBancaria("1002", "Carlos Oliveira", "987.654.321-00", "Centro", "Poupança")
mariana = ContaBancaria("1003", "Mariana Lima", "111.222.333-44", "Savassi", "Corrente")

print("Verificando se as contas foram criadas com saldo zero")

assert ana.saldo == 0
assert carlos.saldo == 0
assert mariana.saldo == 0

print("Mostrando os dados das contas criadas")

print("Conta da Ana")
ana.apresentarDados()

print("Conta do Carlos")
carlos.apresentarDados()

print("Conta da Mariana")
mariana.apresentarDados()


# teste 2 (depositar 500)

print("\nTESTE 2 - Realizando depósito")

print("Depositando R$ 500,00 na conta da Ana")
assert ana.depositar(500) == True

print("Consultando saldo")
ana.consultarSaldo()

assert ana.saldo == 500

print("Conta da Ana após depósito")
ana.apresentarDados()


# teste 3 (sacar 100)

print("\nTESTE 3 - Realizando saque")

print("Sacando R$ 100,00 da conta da Ana")
assert ana.sacar(100) == True

print("Consultando saldo")
ana.consultarSaldo()

assert ana.saldo == 400

print("Conta da Ana após saque")
ana.apresentarDados()


# teste 4 (tentar depositar 0)

print("\nTESTE 4 - Depósito com valor inválido")

print("Tentando depositar R$ 0,00 na conta da Ana")
assert ana.depositar(0) == False

print("Consultando saldo")
ana.consultarSaldo()

assert ana.saldo == 400

print("Conta da Ana após tentativa de depósito")
ana.apresentarDados()

# teste 5 (tentar sacar mais que o saldo)

print("\nTESTE 5 - Sacando valor maior que o saldo")
print("Tentando sacar R$ 1000,00")
assert ana.sacar(1000) == False
print("Consultando saldo")
ana.consultarSaldo()
assert ana.saldo == 400
print("Conta da Ana após tentativa de saque")
ana.apresentarDados()


# teste 6 (alterar o titular da conta)

print("\nTESTE 6 - Alterando titular")
print("Alterando Ana Souza para Ana Maria Souza")
ana.alterarTitular("Ana Maria Souza")
assert ana.titular == "Ana Maria Souza"
print("Conta da Ana com nome atualizado")
ana.apresentarDados()


# teste 7 (bloquear conta e tentar sacar)

print("\nTESTE 7 - Bloqueando a conta")
ana.bloquearConta()
print("Tentando sacar R$ 50,00")
assert ana.sacar(50) == False
assert ana.situacao == "Bloqueada"
assert ana.saldo == 400
print("Conta da Ana bloqueada")
ana.apresentarDados()


# teste 8 (consultar saldo de conta bloqueada)

print("\nTESTE 8 - Consultando conta bloqueada")
print("Consultando saldo da Ana")
ana.consultarSaldo()
assert ana.saldo == 400
print("Mostrando os dados da conta bloqueada")
ana.apresentarDados()


# teste 9 (desbloquear conta e depositar)

print("\nTESTE 9 - Desbloqueando conta")
ana.desbloquearConta()
assert ana.situacao == "Ativa"

print("Depositando R$ 200,00")
assert ana.depositar(200) == True
print("Consultando saldo")
ana.consultarSaldo()
assert ana.saldo == 600
ana.apresentarDados()


# teste 10 (transferir entre contas)

print("\nTESTE 10 - Transferência bancária")

print("Depositando R$ 200,00 para Carlos")
carlos.depositar(200)

print("Depositando R$ 150,00 para Mariana")
mariana.depositar(150)

print("Transferindo R$ 300,00 da Ana para Carlos")
assert ana.transferir(300, carlos) == True

print("Consultando os saldos")
ana.consultarSaldo()
carlos.consultarSaldo()

assert ana.saldo == 300
assert carlos.saldo == 500

print("Contas após transferência")
ana.apresentarDados()
carlos.apresentarDados()


# teste 11 (transferir mais que o saldo)

print("\nTESTE 11 - Transferência com saldo insuficiente")
print("Tentando transferir R$ 500,00 para Mariana")

assert ana.transferir(500, mariana) == False

print("Consultando os saldos")
ana.consultarSaldo()
mariana.consultarSaldo()

assert ana.saldo == 300
assert mariana.saldo == 150

print("Contas após tentativa de transferência")
ana.apresentarDados()
mariana.apresentarDados()


# teste 12 (verificar saldos e emitir relatórios)

print("\nTESTE 12 - Relatórios finais")

print("Relatório da Ana")
ana.emitirRelatorio()

print("Relatório do Carlos")
carlos.emitirRelatorio()

print("Relatório da Mariana")
mariana.emitirRelatorio()

assert ana.saldo == 300
assert carlos.saldo == 500
assert mariana.saldo == 150

assert ana.situacao == "Ativa"
assert carlos.situacao == "Ativa"
assert mariana.situacao == "Ativa"

print("\nTODOS OS 12 TESTES FORAM CONCLUIDOS COM SUCESSO!")
