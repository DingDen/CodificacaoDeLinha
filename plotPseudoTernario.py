import matplotlib.pyplot as plt

def pseudoternario(bits):
    sinal = []
    nivel_atual = 1  
    for bit in bits:
        if bit == '0':
            nivel_atual = -nivel_atual
            sinal.append(nivel_atual)
        else:
            sinal.append(0)
    
    return sinal

def plotPseudoternario(bits, sinal, titulo):
    tempo = list(range(len(sinal)))

    plt.step(tempo, sinal, where='post', label='Sinal Pseudoternário', linewidth=2)
    plt.ylim(-1.5, 1.5)
    plt.xlim(0, len(bits) - 1)
    plt.yticks([-1, 0, 1], ['Negativo', 'Zero', 'Positivo'])
    plt.xticks(range(len(bits)), list(bits))
    plt.title(titulo)
    plt.xlabel('Bits')
    plt.ylabel('Nível do Sinal')
    plt.grid(True)
    plt.legend()
    plt.show()

# Mensagens
bits1 = "1000000001010011"
bits2 = "1110100101000010"

sinal1 = pseudoternario(bits1)
sinal2 = pseudoternario(bits2)

plotPseudoternario(bits1, sinal1, 'Codificação Pseudoternária - Sequência 1')
plotPseudoternario(bits2, sinal2, 'Codificação Pseudoternária - Sequência 2')
