import numpy as np
import matplotlib.pyplot as plt
import math

def calculate_binary_length(a, b, d):
    num_values = (b - a) * 10**d + 1
    m = math.ceil(math.log2(num_values))
    return m

def binary_to_real(chromosome, bounds, num_bits):
    decimal_value = int("".join(map(str, chromosome)), 2)
    real_value = bounds[0] + (bounds[1] - bounds[0]) * decimal_value / (2**num_bits - 1)
    return real_value

def evaluate_population(population, bounds, num_bits):
    fitness = []
    for individual in population:
        split = np.array_split(individual, len(bounds))
        decoded = [binary_to_real(part, bounds[i], num_bits[i]) for i, part in enumerate(split)]
        fitness.append(rastrigin(decoded))
    return np.array(fitness)

def generate_binary_population(population_size, chromosome_length):
    return np.random.randint(2, size=(population_size, chromosome_length))

def rastrigin(X):
    A = 10
    return A * len(X) + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in X])

dimensions = 2
bounds = [(-5.12, 5.12)] * dimensions
num_bits = [calculate_binary_length(bounds[i][0], bounds[i][1], 1) for i in range(dimensions)]
chromosome_length = sum(num_bits)
population_size = 10

population = generate_binary_population(population_size, chromosome_length)

fitness = evaluate_population(population, bounds, num_bits)

print("Initial population:")
print(population)
print("Fitness values:")
print(fitness)

plt.show()
