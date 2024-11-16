import random
import numpy as np


def n_dimensional_mutation(pop, pm=0.1):
    for i in range(len(pop)):
        r = random.uniform(0, 1)
        if r < pm:
            for j in range(len(pop[i])):
                pop[i][j] = 1 if pop[i][j] == 0 else 0
    return pop


def n_dimensional_inversion(pop, pi=0.1):
    for i in range(len(pop)):
        r = random.uniform(0, 1)
        if r < pi:
            punkt1 = random.randint(0, len(pop[i]) - 1)
            punkt2 = random.randint(0, len(pop[i]) - 1)
            if punkt1 > punkt2:
                punkt1, punkt2 = punkt2, punkt1
            pop[i][punkt1:punkt2 + 1] = pop[i][punkt1:punkt2 + 1][::-1]
    return pop


def initialize_population(pop_size, dim):
    return np.random.randint(0, 2, (pop_size, dim))


if __name__ == '__main__':
    pop_size = 10
    dim = 5
    population = initialize_population(pop_size, dim)
    print("Population:\n", population)

    mutation = n_dimensional_mutation(population, pm=0.2)
    inversion = n_dimensional_inversion(population, pi=0.8)

    print("Mutation:\n", mutation)
    print("Inversion:\n", inversion)
