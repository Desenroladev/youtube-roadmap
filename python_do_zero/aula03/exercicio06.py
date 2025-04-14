
# Operadores Logicos
# E (and)
# Ou (or)
# Negação (not)

# Crie um programa que verifica se você esta convidado

convidados = ["maria", "joao", "pedro", "joaquim", "raimundo"]

nome = input("Seu nome por favor: ")
ingresso = input("Seu ingresso por favor (S/N): ").lower() == "S"

# False or True = True
# True and True = True 
# False and True = False
if ingresso or nome in convidados:
    print("Pode entrar!")
else:
    print("Volte para casa!")



