from methode_de_simpson import*
import numpy as np
import timeit
import matplotlib.pyplot as plt

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


