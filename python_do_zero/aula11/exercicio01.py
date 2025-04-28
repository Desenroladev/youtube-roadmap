# tuplas são similares as listas

nomes1 = ["Se", "Inscreve", "no", "Canal"] # mutaveis
nomes2 = ("Se", "Inscreve", "no", "Canal") # imutaveis

nomes1[0] = "Eu já me"
nomes1[1] = "Inscrevi"
print(nomes1)

for nome in nomes2:
    print(nome)

nomes1.append("Novoo item")

print("index: ", nomes2.index("no"))
print("count: ", nomes2.count("no"))

