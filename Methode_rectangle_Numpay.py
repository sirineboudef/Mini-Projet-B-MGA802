import timeit
import numpy as np
from polynome import f
from methode_analytique import integrale_analytique


def integral_rectangle_numpy(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique vectorisée avec NumPy (méthode des rectangles)."""
    h = (b - a) / n
    x = np.linspace(a, b - h, n)  # n points sans le dernier intervalle
    y = f(x, p1, p2, p3, p4)
    return np.sum(y * h)


def erreur_integration(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Erreur absolue entre l'intégrale analytique et numérique classique."""
    exact = integral_analytique(a, b, p1, p2, p3, p4)
    approx = integral_rectangle(a, b, p1, p2, p3, p4, n)
    return abs(exact - approx)


def tester_convergence(a: float, b: float, p1: float, p2: float, p3: float, p4: float):
    """Affiche l'erreur pour des valeurs croissantes de n."""
    print("\nTest de convergence :")
    for n in [10, 100, 1000, 10000, 100000]:
        err = erreur_integration(a, b, p1, p2, p3, p4, n)
        print(f"n={n:<7} erreur={err:.10f}")


def mesurer_temps_execution(a, b, p1, p2, p3, p4, n):
    """Mesure le temps d'exécution de l'intégration numérique classique et vectorisée."""
    temps_classique = timeit.timeit(lambda: integral_rectangle(a, b, p1, p2, p3, p4, n), number=1)
    temps_numpy = timeit.timeit(lambda: integral_rectangle_numpy(a, b, p1, p2, p3, p4, n), number=1)
    print(f"\nTemps d'exécution (classique)  pour n={n} : {temps_classique:.6f} secondes")
    print(f"Temps d'exécution (vectorisé) pour n={n} : {temps_numpy:.6f} secondes")


# valeur fixe pour le coefficient du polynome et limites d'intégration
p1, p2, p3, p4 = 26, 36, 12, 7  # coefficients du polynôme
a, b = -50, 50  # bornes de l'intégrale
n = 10  # nombre de segments pour la méthode des rectangles

exacte = integral_analytique(a, b, p1, p2, p3, p4)
approx = integral_rectangle(a, b, p1, p2, p3, p4, n)
approx_np = integral_rectangle_numpy(a, b, p1, p2, p3, p4, n)
err = abs(exacte - approx)
err_np = abs(exacte - approx_np)

print(f"\nIntégrale analytique   : {exacte}")
print(f"Intégrale Methode rectangle    : {approx}")
print(f"Erreur absolue classique (n={n}): {err}")
print(f"Erreur absolue vectorisée (n={n}): {err_np}")

tester_convergence(a, b, p1, p2, p3, p4)
mesurer_temps_execution(a, b, p1, p2, p3, p4, n)
