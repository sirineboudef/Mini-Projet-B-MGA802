import numpy as np
import timeit
import matplotlib.pyplot as plt
from Methode_rectangle import*
from Methode_rectangle_Numpy import*

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

# Resultats des integrations
# Définition de la fonction polynomiale du 3ème ordre
def f(x):
    return 26 + 36*x + 12*x**2 + 7*x**3  # Exemple: p1=2, p2=3, p3=-1, p4=0.5

# Definition des bornes a et b
a, b = -50, 50  # Bornes

# Definitions du nombre de segments
n = 10       # Nombre de segments
# Calcul de l'integrale avec:
# Python de base
resultat_python = integrale_simpson_python(f, a, b, n)

# NumPy
# Vectorisation: x sera traiter comme tableau NumPy et le calcul vas etre sumultanee a tous ses elements
def f_vectorized(x):
    return 26 + 36*x + 12*x**2 + 7*x**3

resultat_numpy= integrale_simpson_numpy(f_vectorized, a, b, n)

print(f"Résultat avec Python: {resultat_python:.6f}")
print(f"Résultat avec NumPy: {resultat_numpy:.6f}")

# 2eme question

# Dictionnaire des méthodes (implémentées par mes collègues)
methodes = {
    "Rectangles avec Python": integrale_rectangle_python,
    "Rectangles avec NumPy": integrale_rectangle_numpy,
    "Trapèzes avec Python": integrale_trapeze_python,
    "Trapèzes avec NumPy": integrale_trapeze_python,
    "Simpson avec Python": integrale_simpson_python,
    "Simpson avec NumPy": integrale_simpson_numpy
}

# Initialisation des dictionnaires pour inclure les valeurs d'erreurs et temps
erreurs = {}
temps = {}

for nom, methode in methodes.items():
    # Calcul du temps
    t = timeit.timeit(lambda: methodes(f, a, b, n), number=100)

    # Calcul de l'erreur
    exact = integrale_analytique(a, b, p1, p2, p3, p4)
    resultat = methodes(f, a, b, n)
    e = abs(resultat - exact)

    erreurs[nom] = e
    temps[nom] = t * 1000  # en ms

    print(f"{nom}: Erreur = {e:.2e}, Temps = {temps[nom]:.2f} ms")
