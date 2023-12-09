import numpy as np
import matplotlib.pyplot as plt


def distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))


def total_distance(path, pointsInside):
    dist = 0
    for currentIndex in range(len(path) - 1):
        dist += distance(pointsInside[int(path[currentIndex])], pointsInside[int(path[currentIndex + 1])])
    return dist


def generate_points(Nelements):
    x_partition = np.random.uniform(-10, 10, size=(Nelements, 3))
    y_partition = np.random.uniform(0, 20, size=(Nelements, 3))
    z_partition = np.random.uniform(-20, 0, size=(Nelements, 3))
    w_partition = np.random.uniform(0, 20, size=(Nelements, 3))

    x1 = np.array([[20, -20, -20]])
    x1 = np.tile(x1, (Nelements, 1))
    x_partition = x_partition + x1

    x1 = np.array([[-20, 20, 20]])
    x1 = np.tile(x1, (Nelements, 1))
    y_partition = y_partition + x1

    x1 = np.array([[-20, 20, -20]])
    x1 = np.tile(x1, (Nelements, 1))
    z_partition = z_partition + x1

    x1 = np.array([[20, 20, -20]])
    x1 = np.tile(x1, (Nelements, 1))
    w_partition = w_partition + x1
    return np.concatenate((x_partition, y_partition, z_partition, w_partition), axis=0)


K = 20
points = generate_points(K)
I = np.random.permutation(K * 4)
inicial = I[0]
p_origem = points[inicial, :].reshape(1, 3)
points = np.delete(points, inicial, axis=0)

Populacao = np.empty((0, points.shape[0]))
N = 50
for i in range(N):
    individuo = np.random.permutation(points.shape[0]).reshape(1, points.shape[0])
    Populacao = np.concatenate((Populacao, individuo))

vetor_origem = np.tile(np.array([[int(inicial)]]), (N, 1))

# essa matriz pode ser utilizado para aptidao:
caminhos = np.concatenate((vetor_origem, Populacao, vetor_origem), axis=1)


# Algoritmo Genético
def genetic_algorithm(population, pointsGeneric, generationsInside):
    for generation in range(generationsInside):
        fitness = np.array([total_distance(path, pointsGeneric) for path in population])
        sorted_indices = np.argsort(fitness)
        population = population[sorted_indices]

        # Seleção dos melhores indivíduos
        selected_indices = sorted_indices[:N // 2]
        selected_population = population[selected_indices]

        # Cruzamento (crossover)
        crossover_population = []
        for i in range(N // 2):
            parent1 = selected_population[i]
            parent2 = selected_population[np.random.randint(0, N // 2)]
            crossover_point = np.random.randint(1, len(parent1) - 1)
            child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            crossover_population.append(child)

        # Mutação
        mutation_population = np.random.permutation(population)[:N // 4]
        for i in range(N // 4):
            mutation_point1 = np.random.randint(0, len(mutation_population[i]))
            mutation_point2 = np.random.randint(0, len(mutation_population[i]))
            mutation_population[i][mutation_point1], mutation_population[i][mutation_point2] = \
                mutation_population[i][mutation_point2], mutation_population[i][mutation_point1]

        # Nova população
        population = np.concatenate((selected_population, crossover_population, mutation_population))

    best_path = population[0]
    return best_path


# Parâmetros do algoritmo genético
generations = 100

# Inicialização da população
Populacao = np.empty((0, points.shape[0]))
for i in range(N):
    individuo = np.random.permutation(points.shape[0]).reshape(1, points.shape[0])
    Populacao = np.concatenate((Populacao, individuo))

# Execução do algoritmo genético
best_path = genetic_algorithm(Populacao, points, generations)

best_path = np.concatenate(([int(inicial)], best_path, [int(inicial)]))
best_path = best_path.astype(int)  # Converte para inteiros
path_points = points[best_path]

# Visualização do melhor caminho encontrado
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='#248DD2', marker='o')
ax.scatter(p_origem[0:, 0], p_origem[0:, 1], p_origem[0:, 2], c='green', marker='x', linewidth=3, s=30)

# Melhor caminho encontrado
ax.plot(path_points[:, 0], path_points[:, 1], path_points[:, 2], color='r', linewidth=2)

plt.tight_layout()
plt.show()
