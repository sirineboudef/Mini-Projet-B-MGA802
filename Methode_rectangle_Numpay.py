import numpy as np

import timeit

# 2. Fonction polynomiale vectorisée
def f_vect(x: np.ndarray, p1: float, p2: float, p3: float, p4: float) -> np.ndarray:
    """Fonction polynomiale du 3e degré (vectorisée)"""
    return p1 + p2 * x + p3 * x**2 + p4 * x**3

# 3. Intégration par rectangles centrés (vectorisée)
def integral_rectangle(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10) -> float:
    """Méthode des rectangles centrée vectorisée"""

    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)
    y = f_vect(x, p1, p2, p3, p4)
    return np.sum(y) * h

# 4. Mesure du temps d'exécution
def mesurer_temps(a, b, p1, p2, p3, p4, n):
    temps = timeit.timeit(lambda: integral_rectangle(a, b, p1, p2, p3, p4, n), number=1)
    print(f"\n Temps d'exécution rectangle vectorisé, n={n}): {temps:.8f} s")

# === PARAMÈTRES ===
p1, p2, p3, p4 = 26, 36, 12, 7   # Coefficients du polynôme
a, b = -50, 50                  # Bornes d'intégration
n = 100000                      # Nombre de sous-intervalles

# === CALCULS ===
int_exacte = integral_analytique(a, b, p1, p2, p3, p4)
int_centre = integral_rectangle(a, b, p1, p2, p3, p4, n)
erreur = abs(int_centre - int_exacte)

# === AFFICHAGE ===
print("=== Résultats ===")
print(f"Intégrale analytique: {int_exacte:.5f}")
print(f"Intégrale methode rectangle vectorise numpay: {int_centre:.5f}")
print(f"Erreur absolue: {erreur:.5f}")

# === TEMPS D'EXÉCUTION ===
mesurer_temps(a, b, p1, p2, p3, p4, n)
