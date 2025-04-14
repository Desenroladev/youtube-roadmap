
# Operadores Logicos
# E (and)
# Ou (or)
# Negação (not)

# Crie um programa que verifica se você pode sair casa

chovendo = input("Estar chovendo ? (S/N): ").upper() == "S"
if not chovendo:
    print("Pode sair de casa!")
else:
    print("Fique em casa!")

print("####################################")

idade = int(input("Sua idade: "))
if not idade >= 18:
    print("Você é menor de idade!")
else: 
    print("Você é maior de idade")

