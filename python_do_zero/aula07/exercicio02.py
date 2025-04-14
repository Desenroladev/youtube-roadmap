
# Junta dinheiro (Acumulador)

meta = 100
poupanca = 0

while poupanca < meta:
    deposito = float(input("Quanto você vai depositar hoje R$ ?"))
    poupanca += deposito # acumulação ou incremento
    print(f"Saldo da conta: R$ {poupanca:.2f}")

print("Você alcançou a meta! Paranbéns! Continue juntando dinheiro!")
