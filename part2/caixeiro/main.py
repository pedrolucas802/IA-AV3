import numpy as np
import matplotlib.pyplot as plt

def calcular_distancia(ponto1, ponto2):
    return np.sqrt(np.sum((ponto1 - ponto2) ** 2))

def calcular_distancia_total(caminho, pontos_internos):
    dist = 0
    for indice_atual in range(len(caminho) - 1):
        dist += calcular_distancia(pontos_internos[int(caminho[indice_atual])], pontos_internos[int(caminho[indice_atual + 1])])
    return dist

def gerar_pontos(num_elementos):
    x_particao = np.random.uniform(-10, 10, size=(num_elementos, 3))
    y_particao = np.random.uniform(0, 20, size=(num_elementos, 3))
    z_particao = np.random.uniform(-20, 0, size=(num_elementos, 3))
    w_particao = np.random.uniform(0, 20, size=(num_elementos, 3))

    x1 = np.array([[20, -20, -20]])
    x1 = np.tile(x1, (num_elementos, 1))
    x_particao += x1

    x1 = np.array([[-20, 20, 20]])
    x1 = np.tile(x1, (num_elementos, 1))
    y_particao += x1

    x1 = np.array([[-20, 20, -20]])
    x1 = np.tile(x1, (num_elementos, 1))
    z_particao += x1

    x1 = np.array([[20, 20, -20]])
    x1 = np.tile(x1, (num_elementos, 1))
    w_particao += x1
    return np.concatenate((x_particao, y_particao, z_particao, w_particao), axis=0)

def selecao_torneio(fitness, tamanho_torneio):
    indices_selecionados = []
    tamanho_populacao = len(fitness)
    for _ in range(tamanho_populacao):
        indices_torneio = np.random.choice(tamanho_populacao, size=tamanho_torneio, replace=False)
        fitness_torneio = fitness[indices_torneio]
        indice_vencedor = indices_torneio[np.argmin(fitness_torneio)]
        indices_selecionados.append(indice_vencedor)
    return indices_selecionados

def crossover(pai1, pai2):
    ponto_crossover = np.random.randint(1, len(pai1) - 1)
    filho = np.concatenate((pai1[:ponto_crossover], pai2[ponto_crossover:]))
    return filho

def mutacao(individuo, prob_mutacao):
    if np.random.rand() < prob_mutacao:
        ponto_mutacao1 = np.random.randint(0, len(individuo))
        ponto_mutacao2 = np.random.randint(0, len(individuo))
        individuo[ponto_mutacao1], individuo[ponto_mutacao2] = \
            individuo[ponto_mutacao2], individuo[ponto_mutacao1]
    return individuo

#hipeparametros
tamanho_populacao = 100
num_elementos = 20
geracoes = 50
tamanho_torneio = 5
prob_mutacao = 0.01

pontos = gerar_pontos(num_elementos)
permutacao_inicial = np.random.permutation(num_elementos * 4)
inicial = permutacao_inicial[0]
ponto_origem = pontos[inicial, :].reshape(1, 3)
pontos = np.delete(pontos, inicial, axis=0)

populacao = np.empty((0, pontos.shape[0]))
for _ in range(tamanho_populacao):
    individuo = np.random.permutation(pontos.shape[0]).reshape(1, pontos.shape[0])
    populacao = np.concatenate((populacao, individuo))

vetor_origem = np.tile(np.array([[int(inicial)]]), (tamanho_populacao, 1))

caminhos = np.concatenate((vetor_origem, populacao, vetor_origem), axis=1)

# Calcular a distância média entre os pontos
distancias = []
for i in range(num_elementos):
    for j in range(i + 1, num_elementos):
        distancias.append(calcular_distancia(pontos[i], pontos[j]))

distancia_media = np.mean(distancias)

#otimo aceitavel
fator_tolerancia = 5
valor_otimo_aceitavel = fator_tolerancia * distancia_media

geracoes_convergencia = []

def algoritmo_genetico(populacao, pontos_genericos, geracoes_internas, tamanho_torneio, prob_mutacao, valor_otimo_aceitavel):
    melhores_fitness_historico = []

    for geracao in range(geracoes_internas):
        fitness = np.array([calcular_distancia_total(caminho, pontos_genericos) for caminho in populacao])
        indices_ordenados = np.argsort(fitness)
        melhor_caminho = populacao[indices_ordenados[0]]
        melhor_fitness = fitness[indices_ordenados[0]]
        melhores_fitness_historico.append(melhor_fitness)

        if melhor_fitness < valor_otimo_aceitavel:
            print(f"Convergência alcançada na geração {geracao}!")
            geracoes_convergencia.append(geracao)
            break

        indices_selecionados = selecao_torneio(fitness, tamanho_torneio)
        populacao_selecionada = populacao[indices_selecionados]

        populacao_crossover = []
        for i in range(tamanho_populacao // 2):
            pai1 = populacao_selecionada[i]
            pai2 = populacao_selecionada[np.random.randint(0, tamanho_populacao // 2)]
            filho = crossover(pai1, pai2)
            populacao_crossover.append(filho)

        populacao_mutacao = np.random.permutation(populacao)[:tamanho_populacao // 4]
        for i in range(tamanho_populacao // 4):
            populacao_mutacao[i] = mutacao(populacao_mutacao[i], prob_mutacao)

        populacao = np.concatenate((populacao_selecionada, populacao_crossover, populacao_mutacao))

        if geracao % 10 == 0:
            print(f"Geração {geracao}: Melhor custo = {melhor_fitness}")

    return melhor_caminho, melhores_fitness_historico

melhor_caminho_encontrado, historico_melhores_fitness_encontrado = algoritmo_genetico(caminhos, pontos, geracoes, tamanho_torneio, prob_mutacao, valor_otimo_aceitavel)

print(f"Melhor solução encontrada na última geração: {melhor_caminho_encontrado}")

if geracoes_convergencia:
    moda_geracoes = max(set(geracoes_convergencia), key=geracoes_convergencia.count)
    print(f"Moda das gerações de convergência: {moda_geracoes}")
else:
    print("O algoritmo nao encontrou o otimo")

plt.figure()
plt.plot(historico_melhores_fitness_encontrado, label='Melhor Fitness')
plt.xlabel('Geração')
plt.ylabel('Fitness')
plt.title('Evolução ')
plt.legend()
plt.show()

figura = plt.figure(figsize=(10, 8))
eixo = figura.add_subplot(projeção='3d')
eixo.scatter(pontos[:, 0], pontos[:, 1], pontos[:, 2], c='blue', marker='o', label='Pontos')
eixo.scatter(ponto_origem[0:, 0], ponto_origem[0:, 1], ponto_origem[0:, 2], c='green', marker='x', linewidth=3, s=100, label='Origem')

pontos_melhor_caminho = pontos[melhor_caminho_encontrado.astype(int)]
eixo.plot(pontos_melhor_caminho[:, 0], pontos_melhor_caminho[:, 1], pontos_melhor_caminho[:, 2], color='orange', linewidth=3, label='Melhor Caminho')

plt.tight_layout()
plt.show()