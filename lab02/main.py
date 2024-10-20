import numpy as np

from lab01.main import rastrigin


def tournament_selection(population, fitness_func, tournament_size, with_replacement=True, minimize=True):
    new_population = []
    population_size = len(population)
    indices = np.arange(population_size)

    for _ in range(population_size):
        if with_replacement:
            tournament_group_indices = np.random.choice(indices, tournament_size, replace=True)
        else:
            tournament_group_indices = np.random.choice(indices, tournament_size, replace=False)

        tournament_group = [population[i] for i in tournament_group_indices]
        if minimize:
            best_individual = min(tournament_group, key=fitness_func)
        else:
            best_individual = max(tournament_group, key=fitness_func)
        new_population.append(best_individual)

    return new_population


def ranking_selection(population, fitness_func, minimize=True):
    population_size = len(population)

    sorted_population = sorted(population, key=fitness_func, reverse=not minimize)

    new_population = []
    for _ in range(population_size):
        first_rand = np.random.randint(0, population_size)
        second_rand = np.random.randint(0, first_rand + 1)
        index = sorted_population[second_rand]
        new_population.append(index)

    return new_population


def roulette_wheel_selection(population, fitness_func, minimize=True):
    population_size = len(population)

    fitness_values = np.array([fitness_func(individual) for individual in population])

    if minimize:
        fitness_values = np.max(fitness_values) - fitness_values

    total_fitness = np.sum(fitness_values)

    selection_probabilities = fitness_values / total_fitness

    cumulative_probabilities = np.cumsum(selection_probabilities)

    new_population = []
    for _ in range(population_size):
        r = np.random.rand()
        for i, cumulative_probability in enumerate(cumulative_probabilities):
            if r <= cumulative_probability:
                new_population.append(population[i])
                break

    return new_population


if __name__ == '__main__':
    population = [np.array([1, 2]), np.array([3, 4]), np.array([5, 6]), np.array([7, 8])]
    fitness_func = lambda x: rastrigin(x)

    new_population_tournament = tournament_selection(population, fitness_func, tournament_size=2,
                                                     with_replacement=False, minimize=True)
    print(new_population_tournament)

    new_population_ranking = ranking_selection(population, fitness_func, minimize=True)
    print(new_population_ranking)

    new_population_roulette = roulette_wheel_selection(population, fitness_func, minimize=True)
    print(new_population_roulette)
