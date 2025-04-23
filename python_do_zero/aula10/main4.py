
print("🍔 Bem vindo ao restaurante Desenrola Dev! 🍔")

nome = input("Qual seu nome ? ")

print(f"Olá, {nome}! Monte seu Pedido!")

cardapio = ["Hambúrgue", "Batata Frita", "Coca Lata", "Pizza", "Sorvete"]

nome_maior = ""
for nome in cardapio:
    if len(nome) > len(nome_maior):
        nome_maior = nome        

emogis = ["🍔", "🍟", "🥤", "🍕", "🍨"]
precos = [32.90, 12.99, 5.0, 55, 15.50]

pedidos = []
precos_pedido = []
emigis_pedido = []
total = 0

# Mostra o cardapio
print("----------------------------------------------")
for i in range(len(cardapio)):
    nome_produto = cardapio[i]
    diferenca = len(nome_maior) - len(cardapio[i])    
    contador = 0
    while contador < diferenca:
        nome_produto += " "
        contador += 1                    
    print(f"{i+1}. {emogis[i]} {nome_produto} --- R$ {precos[i]:.2f}")
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
    
print("----------------------------------------------")
print("📋 Resumo do pedido:")
nome_maior = ""
for nome in pedidos:
    if len(nome) > len(nome_maior):
        nome_maior = nome  

for i in range(len(pedidos)):
    nome_pedido = pedidos[i]
    diferenca = len(nome_maior) - len(pedidos[i])    
    contador = 0
    while contador < diferenca:
        nome_pedido += " "
        contador += 1          
    print(f"{i+1}. {emigis_pedido[i]} {nome_pedido} --- R$ {precos_pedido[i]:.2f}")
print("----------------------------------------------")
print(f"💸 Total a pagar: R$ {total:.2f}")
print("-----------------'-----'-----'-------------------")
print("Obrigado pela preferência! Volte Sempre!")

