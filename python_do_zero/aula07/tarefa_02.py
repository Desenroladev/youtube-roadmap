
# Exercicio 2
# Crie um programa que peça itens da lista de compras 
# até o usuário digitar "fim".

produtos = []

contador = 0
while contador == 0:
    produto = input("Digite o produto: ")
    if produto.upper() == 'FIM':
        contador = 1
    else:
        produtos.append(produto)

print("Lista de compras: ", produtos)