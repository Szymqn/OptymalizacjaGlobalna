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


def create_population(size, dim):
    return [np.random.uniform(-2, 2, dim) for _ in range(size)]


def select_parents(population, fitness, pk):
    selected = []
    for i, individual in enumerate(population):
        if random.random() < pk:
            selected.append(individual)
    if len(selected) % 2 == 1:
        selected.pop()
    return selected


def genetic_algorithm(dim, generations, pop_size, pk, crossover_type):
    population = create_population(pop_size, dim)
    for generation in range(generations):
        fitness = [rastrigin(individual) for individual in population]
        parents = select_parents(population, fitness, pk)

        offspring = []
        for i in range(0, len(parents), 2):
            if crossover_type == 'single':
                children = single_point_crossover(parents[i], parents[i + 1])
            elif crossover_type == 'two':
                children = two_point_crossover(parents[i], parents[i + 1])
            elif crossover_type == 'uniform':
                children = uniform_crossover(parents[i], parents[i + 1])
            offspring.extend(children)

        population.extend(offspring)
        population.sort(key=rastrigin)
        population = population[:pop_size]

        best_individual = population[0]
        best_fitness = rastrigin(best_individual)
        print(f"Pokolenie {generation}: Najlepsza wartość funkcji = {best_fitness}")

    return best_individual, best_fitness


if __name__ == '__main__':
    dim = 5
    generations = 50
    pop_size = 10
    pk = 0.7
    crossover_type = 'two'

    best_solution, best_value = genetic_algorithm(dim, generations, pop_size, pk, crossover_type)
    print("Najlepsze rozwiązanie:", best_solution)
    print("Najlepsza wartość funkcji:", best_value)
