# AND = só é true quando todas as expressões são verdadeiras
# OR = só é verdadeira se, pelo menos uma das expressões, forem verdadeiras
# NOT = inverte o resultado da expressão 

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

#separando as expreções de comparação por variáveis para ficar mais legível
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (exp_2)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)