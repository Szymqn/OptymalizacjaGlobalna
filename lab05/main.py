import numpy as np


def fitness_function(X):
    A = 10
    return A * len(X) + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])


def initialize_population():
    return np.random.uniform(-10, 10, (POP_SIZE, DIM))


def selection(population, fitness_values, num_parents):
    selected_indices = np.argsort(fitness_values)[:num_parents]
    return population[selected_indices]


def mutate(individual):
    if np.random.rand() < MUTATION_RATE:
        mutation_index = np.random.randint(0, DIM)
        individual[mutation_index] += np.random.normal(0, 1)
    return individual


def crossover(parent1, parent2):
    if np.random.rand() < CROSSOVER_RATE:
        crossover_point = np.random.randint(1, DIM)
        child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
        return child1, child2
    return parent1, parent2


def trivial_succession(old_population, offspring_population):
    return offspring_population


def elitist_succession(old_population, offspring_population, fitness_values, elite_size=2):
    elite_indices = np.argsort(fitness_values)[:elite_size]
    elite_individuals = old_population[elite_indices]
    combined_population = np.vstack((offspring_population, elite_individuals))

    new_fitness = np.array([fitness_function(ind) for ind in combined_population])
    selected_indices = np.argsort(new_fitness)[:POP_SIZE]
    return combined_population[selected_indices]


def elitist_succession_minmax(old_population, offspring_population, min_selection=True):
    combined_population = np.vstack((offspring_population, old_population))
    combined_fitness = np.array([fitness_function(ind) for ind in combined_population])

    if min_selection:
        selected_indices = np.argsort(combined_fitness)[:POP_SIZE]
    else:
        selected_indices = np.argsort(-combined_fitness)[:POP_SIZE]

    return combined_population[selected_indices]


def partial_replacement_succession(old_population, offspring_population, replacement_type, replacement_rate):
    combined_population = np.vstack((old_population, offspring_population))
    combined_fitness = np.array([fitness_function(ind) for ind in combined_population])
    num_replacements = int(POP_SIZE * replacement_rate)

    if replacement_type == "elite":
        worst_indices = np.argsort(combined_fitness)[-num_replacements:]
    elif replacement_type == "squeezed":
        distances = np.sum((combined_population[:, np.newaxis] - combined_population[np.newaxis, :]) ** 2, axis=2)
        np.fill_diagonal(distances, np.inf)
        similar_indices = np.unravel_index(np.argsort(distances, axis=None)[:num_replacements], distances.shape)
        worst_indices = np.unique(similar_indices[0])
    elif replacement_type == "random":
        worst_indices = np.random.choice(np.arange(len(combined_population)), num_replacements, replace=False)
    else:
        raise ValueError("Invalid replacement type")

    remaining_indices = np.setdiff1d(np.arange(len(combined_population)), worst_indices)
    selected_indices = np.argsort(combined_fitness[remaining_indices])[:POP_SIZE]

    return combined_population[remaining_indices][selected_indices]


if __name__ == '__main__':
    POP_SIZE = 10
    GENS = 10
    DIM = 5
    MUTATION_RATE = 0.1
    CROSSOVER_RATE = 0.7
    SUCCESION = "partial_replacement"
    REPLACEMENT_TYPE = "random"
    REPLACEMENT_RATE = 0.5

    population = initialize_population()

    for gen in range(GENS):
        fitness_values = np.array([fitness_function(ind) for ind in population])

        selected_individuals = selection(population, fitness_values, POP_SIZE // 2)

        offspring = []
        for i in range(0, len(selected_individuals), 2):
            parent1, parent2 = selected_individuals[i], selected_individuals[(i + 1) % len(selected_individuals)]
            child1, child2 = crossover(parent1, parent2)
            offspring.append(mutate(child1))
            offspring.append(mutate(child2))
        offspring = np.array(offspring)

        match SUCCESION:
            case "trivial":
                population = trivial_succession(population, offspring)
            case "elitist":
                population = elitist_succession(population, offspring, fitness_values)
            case "elitist_minmax":
                population = elitist_succession_minmax(population, offspring, min_selection=True)
            case "partial_replacement":
                population = partial_replacement_succession(population, offspring, REPLACEMENT_TYPE, REPLACEMENT_RATE)

    print("Ostateczna populacja:", population)
    best_individual = population[np.argmin([fitness_function(ind) for ind in population])]

    print("Najlepszy znaleziony osobnik:", best_individual)
    print("Wartość funkcji przystosowania:", fitness_function(best_individual))
