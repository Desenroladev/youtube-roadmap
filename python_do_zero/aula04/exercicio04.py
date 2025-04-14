# Loop for e enumerate


nomes = ["Antonio", "Edilson", "Thalles", "Antoniel", "Gabriel", "Carlos", "Eduardo"]
# Como concatenar o nome atual com o proximo ? Usando break
for i, nome in enumerate(nomes):
    print(f"{nome} {nomes[i+1]}")
    if i == len(nomes)-2:
        break # Exclusivo de loops for e while