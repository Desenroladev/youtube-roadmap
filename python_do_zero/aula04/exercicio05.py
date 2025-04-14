# Loop for e enumerate


nomes = ["Antonio", "Edilson", "Thalles", "Antoniel", "Gabriel", "Carlos", "Eduardo"]
# Como concatenar o nome atual com o proximo ? Usando continue
for i, nome in enumerate(nomes):
    if nome == "Antoniel" or i == len(nomes)-1:
        continue # Exclusivo de loops for e while
    print(f"{nome} {nomes[i+1]}")