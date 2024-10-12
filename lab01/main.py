import numpy as np
import matplotlib.pyplot as plt


def rastrigin(X):
    A = 10
    return A * len(X) + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])


X = np.array([1, 2, 3])
print(rastrigin(X))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(-5.12, 5.12, 400)
Y = np.linspace(-5.12, 5.12, 400)
X, Y = np.meshgrid(X, Y)
Z = rastrigin([X, Y])

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Rastrigin Function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
