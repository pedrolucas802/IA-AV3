import numpy as np
from random import randint


class Node:
    rainhas = []
    tabuleiro = []
    custo = 0

    def __init__(self, rainhas):
        self.rainhas = rainhas
        self.tabuleiro = np.zeros((8, 8))
        for i in self.rainhas:
            self.tabuleiro[i[1]][i[0]] = 1

        self.custo = self.calcular_custo()

    def calcular_custo(self):
        custo = 0
        for i in range(-7, 7): #soma as diagonais ao custo
            diagonal = np.sum(self.tabuleiro.diagonal(offset=i))
            diagonal_inversa = np.sum(
                np.fliplr(self.tabuleiro).diagonal(offset=i))
            if diagonal > 1:
                custo += diagonal
            if diagonal_inversa > 1:
                custo += diagonal_inversa

        for i in range(0, 8): #soma linhas ao custo
            linha = np.sum(self.tabuleiro[i, :])
            if linha > 1:
                custo += linha

        return custo

    def gerar_vizinhos(self):
        vizinhos = []
        for i in range(0, 8):
            for j in range(0, 8):
                if (self.rainhas[i][1] != j):
                    vizinho_rainhas = self.rainhas.copy()
                    vizinho_rainhas[i][1] = j
                    vizinhos.append(Node(vizinho_rainhas))

        return vizinhos


rainhas = np.array([
    [0, 3],
    [1, 6],
    [2, 2],
    [3, 1],
    [4, 7],
    [5, 2],
    [6, 2],
    [7, 5]
])
no = Node(rainhas)
tentativa = 0
plato = 0

print(no.tabuleiro)


while not (no.custo == 0):
    print("   ---   ")
    print("tentativa", tentativa)
    tentativa += 1
    print("custo atual: ", no.custo)

    vizinhos = no.gerar_vizinhos()
    vizinhos.sort(key=lambda n: n.custo)
    no_aux = vizinhos[0]
    print("gerei ", len(vizinhos), " vizinhos")
    print("o menor vizinho tem custo", no_aux.custo)
    if (no_aux.custo < no.custo):
        no = no_aux
    else:
        print("não consegui encontrar uma opção melhor!! vou escolher qualquer uma")
        plato += 1
        no = vizinhos[randint(0, len(vizinhos)-1)]
    print("\n")



print(("precisei de {} tentativas".format(tentativa)))
print("encontrei {} platôs".format(plato))
print(no.tabuleiro)