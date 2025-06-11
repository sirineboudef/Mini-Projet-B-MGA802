import timeit
from polynome import *

def integral_analytique(a: float, b: float, p1: float, p2: float, p3: float, p4: float):
    """Intégrale analytique de f(x) entre a et b"""
    term1 = p1 * (b - a)
    term2 = p2 * (b ** 2 - a ** 2) / 2
    term3 = p3 * (b ** 3 - a ** 3) / 3
    term4 = p4 * (b ** 4 - a ** 4) / 4
    return term1 + term2 + term3 + term4

def integrale_rectangle_python(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode des rectangles (milieu) sur n segments."""
    h = (b - a) / n
    total = 0
    for i in range(n):
        xi = a + (i + 0.5) * h  # Point milieu de chaque sous-intervalle
        total += f(xi, p1, p2, p3, p4) * h
    return total

def erreur_integration(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Erreur absolue entre l'intégrale analytique et numérique."""
    exact = integral_analytique(a, b, p1, p2, p3, p4)
    approx = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
    return abs(exact - approx)

def tester_convergence(a: float, b: float, p1: float, p2: float, p3: float, p4: float):
    """Affiche l'erreur pour des valeurs croissantes de n."""
    print("\nTest de convergence :")
    for n in [10, 100, 1000, 10000, 100000]:
        err = erreur_integration(a, b, p1, p2, p3, p4, n)
        print(f"n={n:<7} erreur={err:.10f}")

def mesurer_temps_execution(a, b, p1, p2, p3, p4, n):
    """Mesure le temps d'exécution de l'intégration numérique."""
    temps = timeit.timeit(lambda: integrale_rectangle_python(a, b, p1, p2, p3, p4, n), number=1)
    print(f"\nTemps d'exécution pour n={n} : {temps:.6f} secondes")

# === Code principal protégé ===
if __name__ == "__main__":
    # Valeurs fixes pour le polynôme et les bornes d'intégration
    p1, p2, p3, p4 = 26, 36, 12, 7
    a, b = -50, 50
    n = 10

    exacte = integral_analytique(a, b, p1, p2, p3, p4)
    approx = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
    err = abs(exacte - approx)

    print(f"Intégrale analytique   : {exacte}")
    print(f"Intégrale numérique    : {approx}")
    print(f"Erreur absolue (n={n}): {err}")

    tester_convergence(a, b, p1, p2, p3, p4)
    mesurer_temps_execution(a, b, p1, p2, p3, p4, n)
