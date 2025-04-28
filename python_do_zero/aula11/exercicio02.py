
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

match dia:
    case 0:
        print('Domingo')
    case 1:
        print('Segunda Feira')
    case 2:
        print('Terça Feira')
    case 3:
        print('Quarta Feira')
    case 4:
        print('Quinta Feira')     
    case 5:
        print('Sexta Feira')  
    case 6:
        print('Sabado')
    case _: # else/ caso padrão
        print('Dia invalido!')