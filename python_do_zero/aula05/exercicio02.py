# Crie um script que filtrar filmes assistidos com nota maior que 8

filmes = ["Matrix - 9", "Titanic - 7", "Interestelar - 10", "Avatar - 10"]

for filme in filmes:
    aux = filme.split("-")
    nome = aux[0]
    nota = int(aux[1])
    if nota > 8:
        print(f"Gostei do filme: {nome}!")