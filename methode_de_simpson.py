def integrale_simpson_python(f, a, b, n):

    if n % 2 != 0:
        n += 1  # n doit obligatoirement être pair

    h = (b - a) / n
    total = f(a) + f(b)  # bornes d'integration

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:  # Termes pairs
            total += 2 * f(x)
        else:  # Termes impairs
            total += 4 * f(x)

    return (h / 3) * total


import numpy as np

def integrale_simpson_numpy(f, a, b, n):

    if n % 2 != 0:
        n += 1

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Points d'évaluation
    y = f(x)  # Évaluation vectorielle

    # Definition des coefficients alternés 4, 2, 4, 2..., 4, 1
    coeffs = np.ones(n + 1)
    coeffs[1:-1:2] = 4  # Indices impairs
    coeffs[2:-1:2] = 2  # Indices pairs

    return (h / 3) * np.sum(coeffs * y)