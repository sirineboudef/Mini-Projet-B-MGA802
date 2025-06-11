import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import simpson

from methode_analytique import integrale_analytique
from methode_de_simpson import *
from polynome import f
from methode_rectangle_python import integrale_rectangle_python
from Methode_rectangle_Numpy import integrale_rectangle_numpy

def integrale_simpson_scipy(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode de Simpson (SciPy)"""
    x = np.linspace(a, b, n)
    y = f(x, p1, p2, p3, p4)
    return simpson(y, x=x)

if __name__ == "__main__":
    # --- Paramètres ---
    p1, p2, p3, p4 = 26, 36, 12, 7
    a, b = -50, 50
    n = 10

    # --- Calculs initiaux ---
    resultat_python = integrale_simpson_python(a, b, p1, p2, p3, p4, n)
    resultat_numpy = integrale_simpson_numpy(a, b, p1, p2, p3, p4, n)
    resultat_scipy = integrale_simpson_scipy(a, b, p1, p2, p3, p4, n)

    print(f"Résultat avec Simpson Python: {resultat_python:.6f}")
    print(f"Résultat avec Simpson NumPy : {resultat_numpy:.6f}")
    print(f"Résultat avec Simpson SciPy : {resultat_scipy:.6f}")

    # --- Comparaison des méthodes ---
    methods = [
        ("Rectangle Python", integrale_rectangle_python),
        ("Simpson Python", integrale_simpson_python),
        ("Rectangle NumPy", integrale_rectangle_numpy),
        ("Simpson NumPy", integrale_simpson_numpy),
        ("Simpson SciPy", integrale_simpson_scipy),
    ]

    I_exact = integrale_analytique(a, b, p1, p2, p3, p4)
    results = []

    for name, method in methods:
        start = time.perf_counter()
        I = method(a, b, p1, p2, p3, p4, n)
        end = time.perf_counter()
        error = abs(I - I_exact)
        duration = end - start
        results.append((name, I, error, duration))
        print(f"{name:<20} → I = {I:.6f}, erreur = {error:.3e}, durée = {duration:.10f}s")

    # --- Convergence graphique (Python) ---
    n_values = [10, 20, 40, 80, 160, 320, 640, 1280]
    errors_rectangle = []
    errors_simpson = []

    for n in n_values:
        I_rect = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
        I_simp = integrale_simpson_python(a, b, p1, p2, p3, p4, n)
        errors_rectangle.append(abs(I_rect - I_exact))
        errors_simpson.append(abs(I_simp - I_exact))

    plt.figure()
    plt.plot(n_values, errors_rectangle, marker='o', label='Rectangle (Python)')
    plt.plot(n_values, errors_simpson, marker='s', label='Simpson (Python)')
    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence – Méthodes Python")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # --- Convergence graphique (NumPy & SciPy) ---
    errors_rectangle_numpy = []
    errors_simpson_numpy = []
    errors_simpson_scipy = []

    for n in n_values:
        I_rect_np = integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)
        I_simp_np = integrale_simpson_numpy(a, b, p1, p2, p3, p4, n)
        I_simp_sp = integrale_simpson_scipy(a, b, p1, p2, p3, p4, n)
        errors_rectangle_numpy.append(abs(I_rect_np - I_exact))
        errors_simpson_numpy.append(abs(I_simp_np - I_exact))
        errors_simpson_scipy.append(abs(I_simp_sp - I_exact))

    plt.figure()
    plt.plot(n_values, errors_rectangle_numpy, marker='o', label='Rectangle (NumPy)')
    plt.plot(n_values, errors_simpson_numpy, marker='s', label='Simpson (NumPy)')
    plt.plot(n_values, errors_simpson_scipy, marker='s', linestyle=':', label='Simpson (SciPy)')
    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence – NumPy & SciPy")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # --- Temps d'exécution ---
    n_values = [10, 50, 100, 200, 400, 800, 1600, 3200]
    times_rectangle_python = []
    times_rectangle_numpy = []
    times_simpson_python = []
    times_simpson_numpy = []
    times_simpson_scipy = []

    for n in n_values:
        times_rectangle_python.append(timeit(integrale_rectangle_python, a, b, p1, p2, p3, p4, n))
        times_rectangle_numpy.append(timeit(integrale_rectangle_numpy, a, b, p1, p2, p3, p4, n))
        times_simpson_python.append(timeit(integrale_simpson_python, a, b, p1, p2, p3, p4, n))
        times_simpson_numpy.append(timeit(integrale_simpson_numpy, a, b, p1, p2, p3, p4, n))
        times_simpson_scipy.append(timeit(integrale_simpson_scipy, a, b, p1, p2, p3, p4, n))

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times_rectangle_python, marker='o', label="Rectangle (Python)")
    plt.plot(n_values, times_rectangle_numpy, marker='o', linestyle='--', label="Rectangle (NumPy)")
    plt.plot(n_values, times_simpson_python, marker='s', label="Simpson (Python)")
    plt.plot(n_values, times_simpson_numpy, marker='s', linestyle='--', label="Simpson (NumPy)")
    plt.plot(n_values, times_simpson_scipy, marker='s', linestyle=':', label="Simpson (SciPy)")
    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Comparaison des temps – Méthodes numériques")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
