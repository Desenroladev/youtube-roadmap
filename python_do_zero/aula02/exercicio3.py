
# Trabalhando com string

frase = "se inscreve no canal e da like na live"

# Como converter em maiusculo ?
frase_upper = frase.upper()

#print(frase)
#print(frase_upper)

# Como converter para minusculo ?
frase_lower = frase_upper.lower()
#print(frase_lower)

# O que é ignore case ?
# R: Não diferencia uma letra maiuscula de uma menuscula!

# Como fazer substituição de palavras ?
#print(frase.replace('canal', 'Desenrola Dev'))

# Como quebra uma string ?
palavras = frase.split()
#print(palavras) # Lista

# Como inverter uma data ?

data = "26/03/2025"
print("-".join(data.split('/')[::-1]))

# Operadores aritmeticos
# + Soma
# - Subtração
# / Divisão
# * Multiplicação
# // Divisão inteira
# % Resto da divisão
# ** Exponenciação

