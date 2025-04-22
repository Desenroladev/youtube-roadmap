# Exercicio 1

# Crie um programa usando o while que pergunte 
# se chegou nova mensagem (s ou n) 
# e só pare quando a resposta for "n".

while True:
    chegou = input("Chegou nova mensagem ?").lower()

    if chegou == 's':
        print("Chegou uma nova mensagem...")
    elif chegou == 'n':
        break
    else:
        print("Opção invalida!")

print("Terminou o while!!!")