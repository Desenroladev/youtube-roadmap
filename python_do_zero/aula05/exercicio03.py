# Crie um script que liste as roupas sujas

roupas = ["camisa limpa", "calça suja", "meia suja", "casaco limpo"]

limpas = []
sujas = []
for roupa in roupas:
    if "limpa" in roupa or "limpo" in roupa:
        limpas.append(roupa.replace("limpa","").replace("limpo","").strip())
    elif "suja" in roupa:
        sujas.append(roupa.replace("suja", "").strip())
    
print("Limpas: ", limpas)
print("Sujas: ", sujas)
