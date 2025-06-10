from methode_de_simpson import*
import numpy as np
import timeit
import matplotlib.pyplot as plt
from polynome import f
from methodes_des_trapezes import*
from Methode_rectangle_Numpy import*
from methode_de_simpson import*
from methode_simpson_scipy import*

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

# SciPy
resultat_scipy= integrale_simpson_scipy(a, b,26, 36, 12, 7, n)

print(f"Résultat avec Python: {resultat_python:.6f}")
print(f"Résultat avec NumPy: {resultat_numpy:.6f}")
print(f"Résultat avec SciPy: {resultat_scipy:.6f}")


# 2eme question

# Dictionnaire des méthodes (implémentées par mes collègues)
methodes = {
    "Rectangles avec Python": integrale_rectangle_python,
    "Rectangles avec NumPy": integrale_rectangle_numpy,
    "Trapèzes avec Python": integrale_trapeze_python,
    "Trapèzes avec NumPy": integrale_trapeze_numpy,
    "Trapèzes avec SciPy": integrale_trapeze_scipy,
    "Simpson avec Python": integrale_simpson_python,
    "Simpson avec NumPy": integrale_simpson_numpy,
    "Simpson avec SciPy": integrale_simpson_scipy
}

# Initialisation des dictionnaires pour inclure les valeurs d'erreurs et temps
erreurs = {}
temps = {}

for nom, methode in methodes.items():
    # Calcul du temps
    t = timeit.timeit(lambda: methode(f, a, b, n), number=100)

    # Calcul de l'erreur
    resultat = methode(f, a, b, n)
    e = abs(resultat - exact)

    erreurs[nom] = e
    temps[nom] = t * 1000  # en ms

    print(f"{nom}: Erreur = {e:.2e}, Temps = {temps[nom]:.2f} ms")
