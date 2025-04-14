# Vamos um programa que classifica uma pessoa pela idade
# Menor ou igual a 12 anos é uma criança
# Maior que 12 é adolecente
# Maior ou igual a 18 maior idade

idade = int(input("Digite a idade: "))

if idade >= 18:
    print("Você é maior de idade!")
elif idade > 12:
    print("É um adolecente!")    
elif idade >= 1:
    print("É uma criança!")    
elif idade == 0:
    print("É um recem nascido!")
else:
    print("Idade desconhecida!")



