
# Desafio: Quantos anos eu terei daqui a 17 anos ?

# Entrada
idade = int(input("Digite sua idade: "))
diferenca = int(input("Digite a diferença para calculo: "))

# Processamento
idade_futura = idade + diferenca
idade_passado = idade - diferenca

# Saida
print(f"Sua idade daqui {diferenca} anos será {idade_futura}!")
print(f"Sua idade {diferenca} anos atras era {idade_passado}!")



