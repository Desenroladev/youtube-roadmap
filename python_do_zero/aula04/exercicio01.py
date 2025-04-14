# Loops for e while

# O que é um loop ?
# R: É estrutura de repetição
# Para que serve ?
# R: Para repetir instruções

anivesariantes = ["Antonio", "Edilson", "Thalles", "Antoniel", "Gabriel", "Carlos", "Eduardo"]

busca = input("Digite um nome para a pesquisa: ")
achou = False
for nome in anivesariantes:
    if nome.upper() == busca.upper(): # Case insensitive ou ignore case ?
        achou = True
        print("Nome encontrado na lista de aniversariantes!")

if not achou:
    print(f"Nome '{busca}' não encontrado!")

#print(anivesariantes[0])
#print(anivesariantes[1])
#print(anivesariantes[2])
#print(anivesariantes[3])
#print(anivesariantes[4])



"""
a = 1
print(f"O valor de a é: {a}")
a += 1
print(f"O valor de a é: {a}")
a += 1
print(f"O valor de a é: {a}")
a += 1
print(f"O valor de a é: {a}")
a += 1
print(f"O valor de a é: {a}")
"""