import random
import numpy as np

from lab01.main import calculate_binary_length, generate_binary_population


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

    dimensions = 2
    bounds = [(-5.12, 5.12)] * dimensions
    num_bits = [calculate_binary_length(bounds[i][0], bounds[i][1], 1) for i in range(dimensions)]
    chromosome_length = sum(num_bits)
    population_size = 10

    population = generate_binary_population(population_size, chromosome_length)
    print("Population:\n", population)

    mutation = n_dimensional_mutation(population, pm=0.2)
    inversion = n_dimensional_inversion(population, pi=0.8)

    print("Mutation:\n", mutation)
    print("Inversion:\n", inversion)
