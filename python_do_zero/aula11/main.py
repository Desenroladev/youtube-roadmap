

def encontra_nome_maior(produtos):
    maior = {"titulo": ""}
    for produto in produtos:
        if len(produto['titulo']) > len(maior['titulo']):
            maior = produto
    
    return maior

def completa_com_espaco(nome, tamanho):
    return nome + " " * (tamanho - len(nome))


print("🍔 Bem vindo ao restaurante Desenrola Dev! 🍔")

nome = input("Qual seu nome ? ")

print(f"Olá, {nome}! Monte seu Pedido!")

produtos = [
    {"titulo": "Hambúrgue", "emogi": "🍔", "preco": 32.90},
    {"titulo": "Batata Frita", "emogi": "🍟", "preco": 12.99},
    {"titulo": "Coca Lata", "emogi": "🥤", "preco": 5.0},
    {"titulo": "Pizza", "emogi": "🍕", "preco": 55},
    {"titulo": "Sorvete", "emogi": "🍨", "preco": 15.50}
]
nome_maior = encontra_nome_maior(produtos)

pedidos = []
total = 0

# Mostra o cardapio
print("----------------------------------------------")
i = 1
for produto in produtos:
    nome_produto = completa_com_espaco(produto['titulo'], len(nome_maior['titulo']))
    print(f"{i}. {produto['emogi']} {nome_produto} --- R$ {produto['preco']:.2f}")
    i += 1
print("----------------------------------------------")

while True: # Loop infinito
    escolha = input("Digite o número que deseja pedir, ou 'sair' para encerrar: ")

    if escolha.lower() == "sair":
        break # Termina o loop
    elif escolha.isdigit():
        index = int(escolha) - 1
        if index >= 0 and index < len(produtos):
            pedidos.append(produtos[index])            
            total += produtos[index]['preco']
            print(f"✅ {produtos[index]['emogi']} {produtos[index]['titulo']} adicionado ao pedido!")
        else:
            print("❌ Item inválido.")
    else:
        print("❌ Escolha inválida.")
    
print("----------------------------------------------")
print("📋 Resumo do pedido:")
nome_maior = encontra_nome_maior(pedidos)
for i in range(len(pedidos)):
    nome_pedido = completa_com_espaco(pedidos[i]['titulo'], len(nome_maior['titulo']))
    print(f"{i+1}. {pedidos[i]['emogi']} {nome_pedido} --- R$ {pedidos[i]['preco']:.2f}")
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