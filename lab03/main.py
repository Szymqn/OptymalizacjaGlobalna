import random
import numpy as np

from lab01.main import rastrigin


def n_dimensional_mutation(chromosom, pm=0.1):
    for i in range(len(chromosom)):
        r = random.random()
        if r < pm:
            chromosom[i] += random.uniform(-0.1, 0.1)
    return chromosom


def n_dimensional_inversion(chromosom, pi=0.1):
    r = random.random()
    if r < pi:
        punkt1 = random.randint(0, len(chromosom) - 1)
        punkt2 = random.randint(0, len(chromosom) - 1)
        if punkt1 > punkt2:
            punkt1, punkt2 = punkt2, punkt1
        chromosom[punkt1:punkt2+1] = chromosom[punkt1:punkt2+1][::-1]
    return chromosom


if __name__ == '__main__':
    n_dim_chromosome = np.random.rand(10)

    n_dimensional_mutation(n_dim_chromosome, pm=0.2)
    n_dimensional_inversion(n_dim_chromosome, pi=0.2)

    print(n_dim_chromosome)

    rastrigin_chromosome = np.random.uniform(-5.12, 5.12, 10)
    result = rastrigin(rastrigin_chromosome)
    print(result)
