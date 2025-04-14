
transacoes = [8.9, 60, 78, 8.9, 5.6, 7.9, 10.5, 50.0]

# Como calcular o saldo da conta ?

saldo = 0
for valor in transacoes:
    saldo += valor

print(f"Saldo calculado com for: {saldo}")

saldo = 0
i = 0
while i < len(transacoes):
    saldo += transacoes[i]
    i += 1

print(f"Saldo calculado com while: {saldo}")
