
# Estrutura match (Python 3.10+)
# Crie um programa que transforma numero do dias da semana em nomes
# 0 - Domingo
# 1 - Segunda feira
# 2 - Terça feira
# 3 - Quarta Feira
# 4 - Quinta Feira
# 5 - Sexta Feira
# 6 - Sabado

dia = int(input("Digite o número do dia: "))

if dia == 0:
    print('Domingo')
elif dia == 1:
    print('Segunda Feira')
elif dia == 2:
    print('Terça Feira')
elif dia == 3:
    print('Quarta Feira')
elif dia == 4:
    print('Quinta Feira')     
elif dia == 5:
    print('Sexta Feira')  
elif dia == 6:
    print('Sabado')          
else:
    print('Dia invalido!')