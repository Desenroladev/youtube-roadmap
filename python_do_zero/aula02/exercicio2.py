# Trabalhando com lista
# Vamos criar um script para 
# armazena a lista de compras do mês

compras = [
            "Arroz",    # 0 | -9
            "Feijão",   # 1 | -8
            "Sabão",    # 2 | -7
            "Ovo",      # 3 | -6
            "Carne",    # 4 | -5
            "Cerveja",  # 5 | -4
            "Macarrão", # 6 | -3
            "Café",     # 7 | -2
            'Cuzcuz'    # 8 | -1
        ]

#print(compras)

# Como acessar os itens da lista? (f-string)
#print(f"Vou compra: {compras[0]}")

# Como acessar os 2 ultimos itens da lista ?
# lista[inicio:fim:passo] slice
print(compras[-2:]) # retorna os 2 ultimos items
print(compras[::-1]) # Inverte a lista
