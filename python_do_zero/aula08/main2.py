
print("🍔 Bem vindo ao restaurante Desenrola Dev! 🍔")

nome = input("Qual seu nome ? ")

print(f"Olá, {nome}! Monte seu Pedido!")

cardapio = ["Hambúrgue", "Batata Frita", "Coca Lata", "Pizza", "Sorvete"]
emogis = ["🍔", "🍟", "🥤", "🍕", "🍨"]
precos = [32.90, 12.99, 5.0, 55, 15.50]


pedidos = []
precos_pedido = []
emigis_pedido = []
total = 0

# Mostra o cardapio
print("----------------------------------------------")
for i in range(len(cardapio)):
    print(f"{i+1}. {emogis[i]} {cardapio[i]} --- R$ {precos[i]:.2f}")
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
            emigis_pedido.append(emogis[index])
            total += precos[index]
            print(f"✅ {emogis[index]} {cardapio[index]} adicionado ao pedido!")
        else:
            print("❌ Item inválido.")
    else:
        print("❌ Escolha inválida.")
    
print("📋 Resumo do pedido:")
for i in range(len(pedidos)):
    print(f"{i+1}. {emigis_pedido[i]} {pedidos[i]} --- R$ {precos_pedido[i]:.2f}")

print(f"💸 Total a pagar: R$ {total:.2f}")
print("Obrigado pela preferência! Volte Sempre!")


# Desafio Desenrola Dev
# Deixar os preços alinhados como no exemplo abaixo.
#----------------------------------------------
#1. 🍔 Hambúrgue    --- R$ 32.90
#2. 🍟 Batata Frita --- R$ 12.99
#3. 🥤 Coca Lata    --- R$ 5.00
#4. 🍕 Pizza        --- R$ 55.00
#5. 🍨 Sorvete      --- R$ 15.50
#----------------------------------------------

#📋 Resumo do pedido:
#1. 🍔 Hambúrgue --- R$ 32.90
#2. 🍕 Pizza     --- R$ 55.00
#3. 🥤 Coca Lata --- R$ 5.00