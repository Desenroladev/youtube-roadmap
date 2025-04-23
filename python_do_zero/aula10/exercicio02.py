
# RG PET

pets = []
while True:
    print("---------------------------")
    print("1 - Para cadastrar novo PET")
    print("2 - Para listar os PET")
    print("3 - Para sair")
    print("---------------------------")
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        nome = input("Digite o nome: ")
        pet = {
            'nome': nome,
            'raca': input("Digite a raça: "),
            'dono': input("Digite o nome do dono: "),
        }
        pets.append(pet)
        print(f"Pet {pet['nome']} adicionado com sucesso!")
    elif opcao == 2:
        print('--------------------------------')
        if len(pets) == 0:
            print("Nenhum PET cadastrado.")
        for pet in pets:            
            print(f"Nome: {pet['nome']}")
            print(f"Raça: {pet['raca']}")
            print(f"Dono: {pet['dono']}")
        print('--------------------------------')
    elif opcao == 3:
        break
    else:
        print("Opção invalida! Digite novamente!")
