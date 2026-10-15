# Resultados dos testes

```text

--- TESTE 1: Criar conta com saldo zero ---

========== BANCO HORIZONTE ==========
Conta: 1001
Titular: Ana Souza
CPF: 123.456.789-00
Agência: Centro
Tipo: Corrente
Saldo: R$ 0,00
Situação: Ativa
=====================================

--- TESTE 2: Depositar R$ 500,00 em conta ativa ---
Depósito de R$ 500,00 realizado com sucesso!

--- TESTE 3: Sacar R$ 100,00 da mesma conta ---
Saque de R$ 100,00 realizado com sucesso!

--- TESTE 4: Tentar depositar R$ 0,00 ---
Depósito recusado: o valor deve ser maior que zero.

--- TESTE 5: Tentar sacar mais que o saldo ---
Saque recusado: saldo insuficiente.

--- TESTE 6: Alterar o nome do titular ---
Titular alterado com sucesso para: Ana Maria Souza
Alteração recusada: o nome não pode estar vazio.

========== BANCO HORIZONTE ==========
Conta: 1001
Titular: Ana Maria Souza
CPF: 123.456.789-00
Agência: Centro
Tipo: Corrente
Saldo: R$ 400,00
Situação: Ativa
=====================================

--- TESTE 7: Bloquear conta e tentar sacar ---
Conta 1001 bloqueada com sucesso.
Saque recusado: a conta está bloqueada.
Depósito recusado: a conta está bloqueada.

--- TESTE 8: Consultar saldo da conta bloqueada ---
Saldo da conta 1001: R$ 400,00

========== BANCO HORIZONTE ==========
Conta: 1001
Titular: Ana Maria Souza
CPF: 123.456.789-00
Agência: Centro
Tipo: Corrente
Saldo: R$ 400,00
Situação: Bloqueada
=====================================

--- TESTE 9: Desbloquear e realizar depósito ---
Conta 1001 desbloqueada com sucesso.
Depósito de R$ 200,00 realizado com sucesso!

--- TESTE 10: Transferir entre duas contas ativas ---
Depósito de R$ 200,00 realizado com sucesso!
Depósito de R$ 150,00 realizado com sucesso!
Transferência de R$ 300,00 realizada com sucesso! Conta 1001 -> Conta 1002

--- TESTE 11: Tentar transferir mais que o saldo ---
Transferência recusada: saldo insuficiente.

--- VALIDAÇÕES EXTRAS ---
Conta 1003 bloqueada com sucesso.
Transferência recusada: conta de destino bloqueada.
Conta 1003 desbloqueada com sucesso.
Transferência recusada: o valor deve ser maior que zero.
Saque de R$ 50,00 realizado com sucesso!

--- TESTE 12: Verificar saldos e emitir relatórios finais ---
Saldo da conta 1001: R$ 300,00

========== RELATÓRIO DA CONTA ==========
Número da conta: 1001
Titular: Ana Maria Souza
Agência: Centro
Tipo da conta: Corrente
Saldo disponível: R$ 300,00
Situação atual: Ativa
=======================================
Saldo da conta 1002: R$ 500,00

========== RELATÓRIO DA CONTA ==========
Número da conta: 1002
Titular: Carlos Oliveira
Agência: Centro
Tipo da conta: Poupança
Saldo disponível: R$ 500,00
Situação atual: Ativa
=======================================
Saldo da conta 1003: R$ 100,00

========== RELATÓRIO DA CONTA ==========
Número da conta: 1003
Titular: Mariana Lima
Agência: Savassi
Tipo da conta: Corrente
Saldo disponível: R$ 100,00
Situação atual: Ativa
=======================================

SUCESSO: os 12 testes da atividade foram concluídos!
```
# sistema_bancario
