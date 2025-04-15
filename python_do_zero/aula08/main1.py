
print("🍔 Bem vindo ao restaurante Desenrola Dev! 🍔")

nome = input("Qual seu nome ? ")

print(f"Olá, {nome}! Monte seu Pedido!")

cardapio = ["Hambúrgue", "Batata Frita", "Coca Lata", "Pizza", "Sorvete"]
precos = [32.90, 12.99, 5.0, 55, 15.50]

pedidos = []
precos_pedido = []
total = 0
# Mostra o cardapio
print("----------------------------------------------")
for i in range(len(cardapio)):
    print(f"{i+1}. {cardapio[i]} --- R$ {precos[i]:.2f}")
print("----------------------------------------------")

while True: # Loop infinito
    escolha = input("Digite o número que deseja pedir, ou 'sair' para encerrar: ")

    if escolha.lower() == "sair":
        break # Termina o loop
    elif escolha.isdigit():
        index = int(escolha) - 1
        if index >= 0 and index < len(cardapio):
            pedidos.append(cardapio[index])
            precos_pedido.append(precos[index])
            total += precos[index]
            print(f"✅ {cardapio[index]} adicionado ao pedido!")
        else:
            print("❌ Item inválido.")
    else:
        print("❌ Escolha inválida.")
    
print("📋 Resumo do pedido:")
for i in range(len(pedidos)):
    print(f"🍛 {i+1}. {pedidos[i]} --- R$ {precos_pedido[i]:.2f}")

print(f"💸 Total a pagar: R$ {total:.2f}")
print("Obrigado pela preferência! Volte Sempre!")