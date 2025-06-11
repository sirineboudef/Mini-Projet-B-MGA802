import numpy as np
from methode_analytique import integrale_analytique
import timeit
from polynome import *

# Intégration par rectangles centrés (vectorisée)
def integrale_rectangle_numpy(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10) -> float:
    h = (b - a) / n
    x = np.linspace(a + h / 2, b - h / 2, n)
    y = f_vect(x, p1, p2, p3, p4)
    return np.sum(y) * h

# Mesure du temps d'exécution
def mesurer_temps(a, b, p1, p2, p3, p4, n):
    temps = timeit.timeit(lambda: integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n), number=1)
    print(f"\nTemps d'exécution rectangle vectorisé, n={n}: {temps:.8f} s")

# ========== Bloc principal ========== #
if __name__ == "__main__":
    # PARAMÈTRES
    p1, p2, p3, p4 = 26, 36, 12, 7   # Coefficients du polynôme
    a, b = -50, 50                  # Bornes d'intégration
    n = 10                          # Nombre de sous-intervalles

    # CALCULS
    int_exacte = integrale_analytique(a, b, p1, p2, p3, p4)
    int_centre = integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)
    erreur = abs(int_centre - int_exacte)

    # AFFICHAGE
    print("=== Résultats ===")
    print(f"Intégrale analytique: {int_exacte:.5f}")
    print(f"Intégrale méthode rectangle vectorisée NumPy: {int_centre:.5f}")
    print(f"Erreur absolue: {erreur:.5f}")

    # TEMPS D'EXÉCUTION
    mesurer_temps(a, b, p1, p2, p3, p4, n)
