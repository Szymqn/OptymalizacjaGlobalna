import numpy as np
import random


def rastrigin(X):
    A = 10
    return A * len(X) + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])


def single_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    offspring1 = np.concatenate((parent1[:point], parent2[point:]))
    offspring2 = np.concatenate((parent2[:point], parent1[point:]))
    return offspring1, offspring2


def two_point_crossover(parent1, parent2):
    points = sorted(random.sample(range(1, len(parent1)), 2))
    offspring1 = np.concatenate((parent1[:points[0]], parent2[points[0]:points[1]], parent1[points[1]:]))
    offspring2 = np.concatenate((parent2[:points[0]], parent1[points[0]:points[1]], parent2[points[1]:]))
    return offspring1, offspring2


def uniform_crossover(parent1, parent2):
    mask = np.random.randint(2, size=len(parent1))
    offspring1 = np.where(mask, parent1, parent2)
    offspring2 = np.where(mask, parent2, parent1)
    return offspring1, offspring2


def even_crossover(parent1, parent2):
    mask = np.random.randint(2, size=len(parent1))
    offspring1 = np.where(mask == 0, parent1, parent2)
    offspring2 = np.where(mask == 0, parent2, parent1)
    return offspring1, offspring2


def create_population(size):
    return [np.random.randint(0, 2) for _ in range(size)], round(random.random(), 2)


def genetic_algorithm(dim, pop_size, pk, crossover_type):
    populations = []
    indexes = []

    for i in range(dim):
        population, num = create_population(pop_size)
        populations.append(population)

        print("Started population:", population, num)
        if num < pk:
            indexes.append(population)
            populations.remove(population)

    if len(indexes) % 2 == 1:
        indexes.append(random.choice(populations))

    print("Selected indexes:", indexes)

    random.shuffle(indexes)
    paired_indexes = [(indexes[i], indexes[i + 1]) for i in range(0, len(indexes), 2)]

    print("Paired indexes:", paired_indexes)

    crossover = None
    match crossover_type:
        case 'single':
            crossover = single_point_crossover
        case 'two':
            crossover = two_point_crossover
        case 'uniform':
            crossover = uniform_crossover
        case 'even':
            crossover = even_crossover

    for pair in paired_indexes:
        offspring1, offspring2 = crossover(pair[0], pair[1])
        print("Offspring1:", offspring1)
        print("Offspring2:", offspring2)

    return 1, 2


if __name__ == '__main__':
    dim = 10
    pop_size = 10
    pk = 0.5
    crossover_type = 'even'

    best_solution, best_value = genetic_algorithm(dim, pop_size, pk, crossover_type)
    print("Najlepsze rozwiązanie:", best_solution)
    print("Najlepsza wartość funkcji:", best_value)
