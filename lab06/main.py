import random
import numpy as np
import matplotlib.pyplot as plt


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
    results = []
    for epoch in N_EPOCH:
        population = initialize_population(epoch, DIM)

        for p in PM:
            mutations = n_dimensional_mutation(population, pm=p)
            mutations_rate = mutations / epoch * 100

            print(f"Mutation rate, {epoch}/{p}:", mutations_rate)
            results.append((epoch, p, mutations_rate))

    return results


def t_02():
    results = []
    for epoch in N_EPOCH:
        population = initialize_population(epoch, DIM)

        for p in PM:
            inversions = n_dimensional_inversion(population, pm=p)
            inversions_rate = inversions / epoch * 100

            print(f"Mutation rate, {epoch}/{p}:", inversions_rate)
            results.append((epoch, p, inversions_rate))

    return results


def t_03():
    results = []
    for epoch in N_EPOCH:
        for p in PM:
            cross = genetic_algorithm(DIM, epoch, p)
            cross_rate = cross / epoch * 100

            print(f'Cross rate, {epoch}/{p}:', cross_rate)
            results.append((epoch, p, cross_rate))
    return results


def plot_results(results, title, ylabel):
    epochs = sorted(set([r[0] for r in results]))
    pm_values = sorted(set([r[1] for r in results]))

    for pm in pm_values:
        rates = [r[2] for r in results if r[1] == pm]
        plt.plot(epochs, rates, label=f'pm={pm}')

    plt.xlabel('Epochs')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc='upper right')
    plt.show()


if __name__ == '__main__':
    DIM = 10
    N_EPOCH = [10, 50, 100, 200, 500, 1000]
    PM = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    t_01_results = t_01()
    t_02_results = t_02()
    t_03_results = t_03()

    plot_results(t_01_results, 'Mutation Rates', 'Mutation Rate (%)')
    plot_results(t_02_results, 'Inversion Rates', 'Inversion Rate (%)')
    plot_results(t_03_results, 'Crossover Rates', 'Crossover Rate (%)')
