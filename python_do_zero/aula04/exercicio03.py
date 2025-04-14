# Loop for e enumerate


nomes = ["Antonio", "Edilson", "Thalles", "Antoniel", "Gabriel", "Carlos", "Eduardo"]
# Como concatenar o nome atual com o proximo ?
for i, nome in enumerate(nomes):
    if i < len(nomes)-1:
        print(f"{nome} {nomes[i+1]}")