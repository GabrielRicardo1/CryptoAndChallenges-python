print('essa não é de fato uma cifra de cesar. por ser muito simples, decidi me inspirar nela e criar umo decodificador de cifra por coordenadas matriciais. é muito simples, funciona desta forma: ')
print('Para decifrar, você utiliza coordenadas que indicam a posição da letra na matriz de palavras. Por exemplo, se quisermos codificar a letra "T" da palavra "prateleira", a coordenada seria formatada assim:')
print('Coordenada: {{coluna, linha} posição_da_letra}')
print('Portanto, para a letra "T" na palavra "prateleira", a coordenada seria {{1,1} 4}, onde {1,1} representa a posição da palavra na matriz e 4 é a posição da letra "T" dentro da palavra.')
print('Lembre-se de incluir um espaço entre as coordenadas e a posição da letra para garantir que o decodificador funcione corretamente.')

lista_palavras = [
    ["Computador", "Biblioteca", "Relógio", "Telefone", "Escrivaninha"],
    ["Cadeira", "Janela", "Quadro", "Geladeira", "Mochila"]
]

def mostrar_lista():
    for i, linha in enumerate(lista_palavras):
        for j, palavra in enumerate(linha):
            print(f"{i},{j}: {palavra}")

def decifra_coordenadas(coordenadas):
    partes = coordenadas.strip('{}').split('} ')
    linha_coluna = partes[0].split(',')
    linha = int(linha_coluna[0])
    coluna = int(linha_coluna[1])
    posicao_letra = int(partes[1])
    palavra = lista_palavras[linha][coluna]
    
    if posicao_letra < len(palavra):
        letra = palavra[posicao_letra]
        return letra
    else:
        return "" 

def decifra_mensagem(lista_coordenadas):
    mensagem = ""
    for coordenada in lista_coordenadas:
        letra = decifra_coordenadas(coordenada)
        mensagem += letra
    return mensagem

print("lista das palavras:")
mostrar_lista()

coordenadas_usuario = []
while True:
    coordenada = input("Digite uma coordenada ou 'fim' para terminar de usar o decodificadpr: ")
    if coordenada.lower() == 'fim':
        break
    coordenadas_usuario.append(coordenada)

mensagem_decifrada = decifra_mensagem(coordenadas_usuario)
print(f"A mensagem decifrada é: '{mensagem_decifrada}'")

# testa o código com as coordenadas aí de baixo:

# {{0,3} 1} 
# {{1,1} 1} 
# {{0,1} 1} 

