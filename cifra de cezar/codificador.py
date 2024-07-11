# o codificador é muito mais simples de usar, aliás acho que nem tem muito o que te explicar aqui. comece vendo o código pelo decodificador mesmo!
lista_palavras = [
    ["Computador", "Biblioteca", "Relógio", "Telefone", "Escrivaninha"],
    ["Cadeira", "Janela", "Quadro", "Geladeira", "Mochila"]
]

def mostra_lista():
    
    for i, linha in enumerate(lista_palavras):
        for j, palavra in enumerate(linha):
            print(f"{i},{j}: {palavra}")

def encontrar_letra(palavra, letra):
    
    try:
        posicao = palavra.index(letra)
        return posicao
    except ValueError:
        return None

def codificar_mensagem(mensagem):
    coordenadas = []
    for letra in mensagem:
        encontrou = False
        for i, linha in enumerate(lista_palavras):
            for j, palavra in enumerate(linha):
                posicao_letra = encontrar_letra(palavra, letra)
                if posicao_letra is not None:
                    coordenada = f"{{{i},{j}}} {posicao_letra}"
                    coordenadas.append(coordenada)
                    encontrou = True
                    break
            if encontrou:
                break
    return coordenadas

print("lista das palavras:")
mostra_lista()

mensagem = input("Digite a mensagem a ser codidicada: ")

coordenadas_codificadas = codificar_mensagem(mensagem)
print("Coordenadas codificadas:")
for coordenada in coordenadas_codificadas:
    print(coordenada)
