
# Lista
nomes = ["João", "Pedro"]

# Estrutura de dados dicionario
# Chave e Valor
rg_pet = {
    "numero" : 8786689304,
    "nome" : "Scoob",
    "data_nascimento" : "01/01/2025",
    "dono" : "Francisco Raimundo",
    "endereco" : "Rua da areia branca, 597"
}

print("Número:", rg_pet['numero'])
print("Nome:", rg_pet['nome'])
print("Data Nascimento:", rg_pet['data_nascimento'])
print("Dono:", rg_pet['dono'])
print("Endereço:", rg_pet['endereco'])

if 'peso' in rg_pet: # verifica se uma chave existe
    print("Peso1:", rg_pet.get('peso', 'Desconhecido')) # acessando com .get

rg_pet['peso'] = 20 # atribuir um novo valor ao dicionario

if 'peso' in rg_pet:
    print("Peso2:", rg_pet['peso']) # acessando dados com ['chave']

pessoa = {
    "nome": "Joao Amancio",
    "cpf": "0000000000",
    "endereco": {
        "numero": 78,
        "cep": 89722500,
        "bairro": "Itapebusu",
        "cidade": "Sao Paulo",
        "uf": "SP"
    },
    "telefones": ["85978421212", "979821133"]
}

matriz = [["Antoniel", "Raimundo"], ["Lima", "Joao"]]
#print(matriz) # 2x2

print("-------------------------------------------")
print("Endereço:", pessoa['endereco'])
print("UF:", pessoa['endereco']['uf'])
print("Telefones:", pessoa['telefones'])


pessoas = [pessoa, pessoa, pessoa]
print("\n")
print("\n")
print("\n")
print("\n")
for p in pessoas:
    print(p)