import numpy as np
from colorama import Fore, Style


def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            if valor == 1:
                print(f"{Fore.RED}{valor} ", end="")
            else:
                print(f"{Style.RESET_ALL}{valor} ", end="")
        print()


def verificar_coluna(tabuleiro, coluna, linha):
    for i in range(linha):
        if tabuleiro[i][coluna] == 1:
            return False
    return True


def verificar_diagonal(tabuleiro, coluna, linha):
    for i, j in zip(range(linha - 1, -1, -1), range(coluna - 1, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False
    for i, j in zip(range(linha - 1, -1, -1), range(coluna + 1, len(tabuleiro))):
        if tabuleiro[i][j] == 1:
            return False
    return True


class Node:
    def __init__(self, rainhas):
        self.rainhas = np.array(rainhas)
        self.tabuleiro = np.zeros((8, 8))
        for i in self.rainhas:
            self.tabuleiro[i[1]][i[0]] = 1

        self.custo = self.calcular_custo()

    def calcular_custo(self):
        custo = 0
        for i in range(-7, 7):
            diagonal = np.sum(self.tabuleiro.diagonal(offset=i))
            diagonal_inversa = np.sum(np.fliplr(self.tabuleiro).diagonal(offset=i))
            if diagonal > 1:
                custo += diagonal
            if diagonal_inversa > 1:
                custo += diagonal_inversa

        for i in range(8):
            linha = np.sum(self.tabuleiro[i, :])
            if linha > 1:
                custo += linha

        return custo

    def gerar_vizinhos(self):
        vizinhos = []
        for i in range(8):
            for j in range(8):
                if self.rainhas[i][1] != j:
                    vizinho_rainhas = self.rainhas.copy()
                    vizinho_rainhas[i][1] = j
                    vizinhos.append(Node(vizinho_rainhas))

        return vizinhos


def encontrar_solucoes(tabuleiro, linha):
    if linha == len(tabuleiro):
        return [(tabuleiro.copy(), 0)]

    solucoes = []

    for coluna in range(len(tabuleiro)):
        if verificar_coluna(tabuleiro, coluna, linha) and verificar_diagonal(tabuleiro, coluna, linha):
            tabuleiro[linha][coluna] = 1
            solucoes.extend(encontrar_solucoes(tabuleiro, linha + 1))
            tabuleiro[linha][coluna] = 0

    return solucoes


solucoes_unicas = set()

todas_solucoes = encontrar_solucoes(np.zeros((8, 8)), 0)

for i, (solucao, custo) in enumerate(todas_solucoes, 1):
    print(f"\nSolução {i} - Custo: {custo}")
    imprimir_tabuleiro(solucao)

print(f"\nNúmero de soluções únicas encontradas: {len(todas_solucoes)}")