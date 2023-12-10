import random

def cromossomo_aleatorio(tamanho):
    return [random.randint(0, tamanho - 1) for _ in range(tamanho)]

def aptidao(cromossomo, max_aptidao):
    colisoes_horizontais = (
        sum([cromossomo.count(rainha) - 1 for rainha in cromossomo]) / 2
    )
    colisoes_diagonais = 0

    n = len(cromossomo)
    diagonal_esquerda = [0] * (2 * n - 1)
    diagonal_direita = [0] * (2 * n - 1)
    for i in range(n):
        diagonal_esquerda[i + cromossomo[i] - 1] += 1
        diagonal_direita[len(cromossomo) - i + cromossomo[i] - 2] += 1

    colisoes_diagonais = 0
    for i in range(2 * n - 1):
        contador = 0
        if diagonal_esquerda[i] > 1:
            contador += diagonal_esquerda[i] - 1
        if diagonal_direita[i] > 1:
            contador += diagonal_direita[i] - 1
        colisoes_diagonais += contador

    return int(max_aptidao - (colisoes_horizontais + colisoes_diagonais))

def crossover(x, y):
    n = len(x)
    filho = [0] * n
    for i in range(n):
        c = random.randint(0, 1)
        if c < 0.5:
            filho[i] = x[i]
        else:
            filho[i] = y[i]
    return filho

def mutacao(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(0, n - 1)
    x[c] = m
    return x

def probabilidade(cromossomo, max_aptidao):
    return aptidao(cromossomo, max_aptidao) / max_aptidao

#roleta
def escolha_aleatoria(populacao, probabilidades):
    populacao_com_probabilidade = zip(populacao, probabilidades)
    total = sum(w for c, w in populacao_com_probabilidade)
    r = random.uniform(0, total)
    ate = 0
    for c, w in zip(populacao, probabilidades):
        if ate + w >= r:
            return c
        ate += w
    assert False, "Não deveria chegar aqui"

def algoritmo_genetico_rainhas(populacao, max_aptidao):
    probabilidade_mutacao = 0.1
    nova_populacao = []
    populacao_ordenada = []
    probabilidades = []
    for cromossomo in populacao:
        f = aptidao(cromossomo, max_aptidao)
        probabilidades.append(f / max_aptidao)
        populacao_ordenada.append([f, cromossomo])

    populacao_ordenada.sort(reverse=True)

    # Elitismo
    nova_populacao.append(populacao_ordenada[0][1])  # o melhor gen
    nova_populacao.append(populacao_ordenada[-1][1])  # o pior gen

    for i in range(len(populacao) - 2):
        cromossomo_1 = escolha_aleatoria(populacao, probabilidades)
        cromossomo_2 = escolha_aleatoria(populacao, probabilidades)

        # Criando dois novos cromossomos a partir de 2 cromossomos
        filho = crossover(cromossomo_1, cromossomo_2)

        # Mutação
        if random.random() < probabilidade_mutacao:
            filho = mutacao(filho)

        nova_populacao.append(filho)
        if aptidao(filho, max_aptidao) == max_aptidao:
            break
    return nova_populacao

def imprimir_cromossomo(crom, max_aptidao):
    print(
        "Cromossomo = {},  Aptidão = {}".format(str(crom), aptidao(crom, max_aptidao))
    )

def imprimir_tabuleiro(crom):
    tabuleiro = []

    for x in range(8):
        tabuleiro.append(["x"] * 8)

    for i in range(8):
        tabuleiro[crom[i]][i] = "Q"

    def imprimir_tabuleiro(tabuleiro):
        for linha in tabuleiro:
            print(" ".join(linha))

    print()
    imprimir_tabuleiro(tabuleiro)

def rainhas_geneticas():
    TAMANHO_POPULACAO = 50
    nq = 8
    max_geracoes = 2500
    max_aptidao = (nq * (nq - 1)) / 2  # 8*7/2 = 28
    populacao = [cromossomo_aleatorio(nq) for _ in range(TAMANHO_POPULACAO)]

    geracao = 1
    solucoes_encontradas = 0
    while solucoes_encontradas < 92 or geracao == max_geracoes:  # Continua até que todas as 92 soluções sejam encontradas
        populacao = algoritmo_genetico_rainhas(populacao, max_aptidao)
        if geracao % 10 == 0:
            print("=== Geração {} ===".format(geracao))
            print(
                "Aptidão Máxima = {}".format(
                    max([aptidao(crom, max_aptidao) for crom in populacao])
                )
            )
        geracao += 1

        aptidoes_dos_cromossomos = [aptidao(crom, max_aptidao) for crom in populacao]

        if max_aptidao in aptidoes_dos_cromossomos:
            melhores_cromossomos = populacao[
                aptidoes_dos_cromossomos.index(max(aptidoes_dos_cromossomos))
            ]

            # print("\nSolução {}:".format(solucoes_encontradas + 1))
            imprimir_cromossomo(melhores_cromossomos, max_aptidao)
            imprimir_tabuleiro(melhores_cromossomos)

            solucoes_encontradas += 1

    # print("\nEncontrou todas as 92 soluções em {} gerações.".format(geracao - 1))

    return geracao - 1

resultados = []
iteracao = 0
for _ in range(5):
    resultado_atual = rainhas_geneticas()
    resultados.append(resultado_atual)
    iteracao += 1
    print(str(iteracao))

print("resultado:")
print(resultados)