import matplotlib.pyplot as plt
from random import randint

# 0: sem transição; 1: transição positivo/negativo
def NRZI_Code(lista_de_bits: list, nivel_inicial: int):
    lista_transicao = []
    
    if (nivel_inicial == -1):
        # -1: Sinal Negativo; 1: Sinal Positivo
        transicao = nivel_inicial
        lista_transicao.append(transicao) 
        for i in range(len(lista_de_bits)):
            if (lista_de_bits[i] == 0 and transicao == -1):
                lista_transicao.append(-1)
            elif (lista_de_bits[i] == 0 and transicao == 1):
                lista_transicao.append(1)
            elif (lista_de_bits[i] == 1 and transicao == -1):
                lista_transicao.append(1)
                transicao = 1
            elif (lista_de_bits[i] == 1 and transicao == 1):
                lista_transicao.append(-1)
                transicao = -1
    
    elif (nivel_inicial == 1):
        # -1: Sinal Negativo; 1: Sinal Positivo
        transicao = nivel_inicial
        lista_transicao.append(transicao)
        for i in range(len(lista_de_bits)):
            if (lista_de_bits[i] == 0 and transicao == -1):
                lista_transicao.append(-1)
            elif (lista_de_bits[i] == 0 and transicao == 1):
                lista_transicao.append(1)
            elif (lista_de_bits[i] == 1 and transicao == -1):
                lista_transicao.append(1)
                transicao = 1
            elif (lista_de_bits[i] == 1 and transicao == 1):
                lista_transicao.append(-1)
                transicao = -1
    
    return lista_transicao

def plotGraphNRZI(lista_bits: list):
    listaNivel = [-1, 1] # -1: baixo | 1: alto
    listaNivel_S = ["Negativo", "Positivo"]
    
    # Escolhe um nível inicial aleatório 
    listaTransicao = NRZI_Code(lista_bits, listaNivel[randint(0, 1)])
    
    # Plot por passo: y se mantém constante até o próximo x, onde ocorre a transição
    plt.step(range(-1, len(listaTransicao) - 1), listaTransicao, color="blue", where="post")
    
    # Rótulação do gráfico
    plt.title("Codificação NRZI")
    plt.xlabel("Bits")
    plt.ylabel("Nivel do sinal")

    plt.xticks(range(len(lista_bits)), lista_bits) # Representação dos bits no eixo x

    plt.yticks(listaNivel, listaNivel_S) # Representação do nível do sinal no eixo y

    plt.show() # Exibe o gráfico

# Teste 1
lista1bits = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1]
plotGraphNRZI(lista1bits)

# Teste 2
lista2bits = [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
plotGraphNRZI(lista2bits)