
# Operadores Logicos
# E (and)
# Ou (or)
# Negação (not)

# Crie um programa que verifica se você pode dirigir

idade = int(input("Digite sua idade: "))
tem_habilitacao = input("Tem habilitação ? (S/N)").upper() == "S"

if idade >= 18 and tem_habilitacao:
    print("Você pode dirigir!")



