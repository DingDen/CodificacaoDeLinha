import matplotlib.pyplot as plt

def alg4B3T(lista_bits: list):
    lista4B = []
    simbolo = []
    lista3T = []
    
    for i in range(len(lista_bits)):
        lista4B.append(lista_bits[i])

        if(len(lista4B) == 4):
            ultimo_simbolo_lista = lista3T[-1] if len(lista3T) > 0 else 1
            simbolo = tabela_Jesse(lista4B, ultimo_simbolo_lista) #, 0 if i == 0 else lista4B[i-1])

            lista3T.append(simbolo[0])
            lista3T.append(simbolo[1])
            lista3T.append(simbolo[2])
            lista3T.append(simbolo[2]) # Extensão para plotagem
            lista4B = []
            simbolo = []

    return lista3T
    
def tabela_Jesse(lista_bits: list, ultimo_simbolo_lista:int) -> list:#, ultimo_simbolo_lista:int = 0) -> list:
    lista_simbolos =  "".join(map(str, lista_bits))
    chaves_simbolos = {
        "0000": [0,-1,1],
        "0001": [-1,1,0],
        "0010": [-1,0,1],
        "0011": [1,-1,1] if ultimo_simbolo_lista > 0 else [-1,1,-1],
        "0100": [0,1,1] if ultimo_simbolo_lista > 0 else [0,-1,-1],
        "0101": [0,1,0] if ultimo_simbolo_lista > 0 else [0,-1,0],
        "0110": [0,0,1] if ultimo_simbolo_lista > 0 else [0,0,-1],
        "0111": [-1,1,1] if ultimo_simbolo_lista > 0 else [0,0,-1],
        "1000": [0,1,-1],
        "1001": [1,-1,0],
        "1010": [1,0,-1],
        "1011": [1,0,0] if ultimo_simbolo_lista > 0 else [-1,0,0],
        "1100": [1,0,1] if ultimo_simbolo_lista > 0 else [-1,0,-1],
        "1101": [1,1,0] if ultimo_simbolo_lista > 0 else [-1,-1,0],
        "1110": [1,1,-1] if ultimo_simbolo_lista > 0 else [-1,-1,1],
        "1111": [1,1,1] if ultimo_simbolo_lista > 0 else [-1,-1,-1],
    }

    for chave in chaves_simbolos:
        #if chaves_simbolos[chave] == lista_simbolos:
        if chave == lista_simbolos:
            return chaves_simbolos[chave]

def plotGraph4B3T(lista_bits: list):
    lista4B3T = alg4B3T(lista_bits)

    listaSinal = ["Negativo", "0", "Positivo"] # Conectar depois no lugar de 1, 0 e -1
    
    plt.step(range(len(lista4B3T)), lista4B3T, color="blue", where="post")

    for i in range(4, len(lista_bits), 4):
        plt.axvline(x=i-0.5, color='red', linestyle='--')
    
    # Rótulação do gráfico
    plt.title("4B3T Codificação")

    plt.step(range(len(lista4B3T)), lista4B3T, color="blue", where="post")
    
    # Rótulação do gráfico
    plt.title("NRZI Codificação")

    plt.xlabel("Tempo (bits)")
    plt.ylabel("Nivel do sinal")

    plt.xticks(range(len(lista_bits)), lista_bits) # Representação dos bits no eixo x

    plt.yticks(lista4B3T) # Representação do nível do sinal no eixo y
    
    plt.grid(True)

    plt.show() # Exibe o gráfico

lista1 = [1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1]
plotGraph4B3T(lista1)