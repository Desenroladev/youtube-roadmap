
# Exercicio 3
# Crie um jogo onde o usuário precisa adivinhar um número 
# entre 1 e 10.

import random

secreto = random.randint(1, 10)
while True:
    numero = int(input("Digite um número entre 1 e 10: "))
    if secreto == numero:
        break
    else:
        print("Número invalido tente novamente!")





