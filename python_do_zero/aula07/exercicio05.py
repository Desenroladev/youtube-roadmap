
comida_salgada = False

while not comida_salgada:
    print("Provando a comida...")
    comida_salgada = input("Está no ponto ? (S/N)").upper() == "S"

print("Comida aprovada!")

