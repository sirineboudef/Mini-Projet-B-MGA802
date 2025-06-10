import numpy as np
import matplotlib.pyplot as plt
import time

# Définition des coefficients du polynôme
p1, p2, p3, p4 = 26, 36, 12, 7


# Fonction polynomiale
def f_bis(x: float):
    return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3


# Version vectorisée pour NumPy
def f_vectorized(x):
    return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3


# Méthode de Simpson avec Python pur
def integrale_simpson_python(f, a, b, n):
    if n % 2 != 0:
        n += 1  # n doit être pair

    h = (b - a) / n
    total = f_bis(a) + f_bis(b)  # Termes aux bornes

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            total += 2 * f_bis(x)  # Termes pairs
        else:
            total += 4 * f_bis(x)  # Termes impairs

    return (h / 3) * total


# Méthode de Simpson avec NumPy
def integrale_simpson_numpy(f, a, b, n):
    if n % 2 != 0:
        n += 1

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f_bis(x)

    # Création des coefficients
    coeffs = np.ones(n + 1)
    coeffs[1:-1:2] = 4  # Termes impairs
    coeffs[2:-1:2] = 2  # Termes pairs

    return (h / 3) * np.sum(coeffs * y)


# Paramètres d'intégration
a, b = -50, 50
n = 10

# Calculs et affichage
resultat_python = integrale_simpson_python(f_bis, a, b, n)
resultat_numpy = integrale_simpson_numpy(f_vectorized, a, b, n)

print(f"Résultat avec Python: {resultat_python:.6f}")
print(f"Résultat avec NumPy: {resultat_numpy:.6f}")

# 2eme question
"""Comparez la précision (erreur) et le temps d’exécution de la méthode de Simpson avec
 ceux de la méthode des rectangles et la méthode des trapèzes pour un nombre de seg
ments donné dans les cas de Python et NumPy."""
