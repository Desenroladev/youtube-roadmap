

def encontra_nome_maior(nomes):
    maior = ""
    for nome in nomes:
        if len(nome) > len(maior):
            maior = nome
    
    return maior

def completa_com_espaco(nome, tamanho):
    diferenca = tamanho - len(nome)    
    contador = 0
    while contador < diferenca:
        nome += " "
        contador += 1

    return nome



print("🍔 Bem vindo ao restaurante Desenrola Dev! 🍔")

nome = input("Qual seu nome ? ")

print(f"Olá, {nome}! Monte seu Pedido!")

cardapio = ["Hambúrgue", "Batata Frita", "Coca Lata", "Pizza", "Sorvete"]

nome_maior = encontra_nome_maior(cardapio)

emogis = ["🍔", "🍟", "🥤", "🍕", "🍨"]
precos = [32.90, 12.99, 5.0, 55, 15.50]

pedidos = []
precos_pedido = []
emigis_pedido = []
total = 0

# Mostra o cardapio
print("----------------------------------------------")
for i in range(len(cardapio)):
    nome_produto = completa_com_espaco(cardapio[i], len(nome_maior))
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
nome_maior = encontra_nome_maior(pedidos)
for i in range(len(pedidos)):
    nome_pedido = completa_com_espaco(pedidos[i], len(nome_maior))
    print(f"{i+1}. {emigis_pedido[i]} {nome_pedido} --- R$ {precos_pedido[i]:.2f}")
print("----------------------------------------------")
print(f"💸 Total a pagar: R$ {total:.2f}")
print("-----------------'-----'-----'-------------------")
print("Obrigado pela preferência! Volte Sempre!")


# Desafio Desenrola Dev
# Usar dicionario para guarda os cadastros do menu
#----------------------------------------------
#1. 🍔 Hambúrgue    --- R$ 32.90
#2. 🍟 Batata Frita --- R$ 12.99
#3. 🥤 Coca Lata    --- R$ 5.00
#4. 🍕 Pizza        --- R$ 55.00
#5. 🍨 Sorvete      --- R$ 15.50
#----------------------------------------------

# Usar dicionario para armazerna os pedidos
#----------------------------------------------
#📋 Resumo do pedido:
#1. 🍔 Hambúrgue --- R$ 32.90
#2. 🍕 Pizza     --- R$ 55.00
#3. 🥤 Coca Lata --- R$ 5.00
#----------------------------------------------