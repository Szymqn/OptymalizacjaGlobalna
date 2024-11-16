import random
import numpy as np


def initialize_population(pop_size, dim):
    return np.random.randint(0, 2, (pop_size, dim))


def n_dimensional_mutation(pop, pm=0.1):
    mutated = 0

    for i in range(len(pop)):
        r = random.uniform(0, 1)
        if r < pm:
            for j in range(len(pop[i])):
                pop[i][j] = 1 if pop[i][j] == 0 else 0
            mutated += 1

    return mutated


def n_dimensional_inversion(pop, pm=0.1):
    inversion = 0

    for i in range(len(pop)):
        r = random.uniform(0, 1)
        if r < pm:
            punkt1 = random.randint(0, len(pop[i]) - 1)
            punkt2 = random.randint(0, len(pop[i]) - 1)
            if punkt1 > punkt2:
                punkt1, punkt2 = punkt2, punkt1
            pop[i][punkt1:punkt2 + 1] = pop[i][punkt1:punkt2 + 1][::-1]
            inversion += 1
    return inversion


def create_population(size):
    return [np.random.randint(0, 2) for _ in range(size)], round(random.random(), 2)


def genetic_algorithm(dim, pop_size, pk):
    populations = []
    indexes = []
    cross = 0

    for i in range(dim):
        population, num = create_population(pop_size)
        populations.append(population)

        if num < pk:
            indexes.append(population)
            populations.remove(population)
            cross += 1

    return cross


def t_01():
    for epoch in N_EPOCH:
        population = initialize_population(epoch, DIM)

        for p in PM:
            mutations = n_dimensional_mutation(population, pm=p)

            print(f"Mutation rate, {epoch}/{p}:", mutations/epoch*100)


def t_02():
    for epoch in N_EPOCH:
        population = initialize_population(epoch, DIM)

        for p in PM:
            mutations = n_dimensional_inversion(population, pm=p)

            print(f"Mutation rate, {epoch}/{p}:", mutations / epoch * 100)


def t_03():
    for epoch in N_EPOCH:
        for p in PM:
            cross = genetic_algorithm(DIM, epoch, p)

            print(f'Cross rate, {epoch}/{p}:', cross/epoch*100)


if __name__ == '__main__':
    DIM = 10
    N_EPOCH = [10, 50, 100, 200, 500, 1000]
    PM = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    # t_01()
    t_02()
    # t_03()
