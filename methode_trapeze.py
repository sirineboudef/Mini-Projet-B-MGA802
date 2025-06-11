# Importations necessaires
from polynome import f  # f(x, p1, p2, p3, p4)
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from methode_analytique import integrale_analytique
from methode_rectangle_python import integrale_rectangle_python
from Methode_rectangle_Numpy import integrale_rectangle_numpy


# Fonction pour calculer l'integrale avec la méthode du trapèze (Python de base)
def integrale_trapeze_python(a, b, p1, p2, p3, p4, n=10):
    pas = (b - a) / n
    total = 0.5 * (f(a, p1, p2, p3, p4) + f(b, p1, p2, p3, p4))
    for i in range(1, n):
        x = a + i * pas
        total += f(x, p1, p2, p3, p4)
    return pas * total

# Fonction pour calculer l'integrale avec la méthode du trapèze (NumPy)
def integrale_trapeze_numpy(a, b, p1, p2, p3, p4, n=10):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = p1 + p2 * x + p3 * x**2 + p4 * x**3
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))


# Définition des coefficients et bornes
p1, p2, p3, p4 = 26, 36, 12, 7
a, b = -50, 50
n = 10

# === Code principal ===
if __name__ == "__main__":
    I_exact = integrale_analytique(a, b, p1, p2, p3, p4)

    # Méthodes à comparer
    methods = [
        ("Rectangle Python", integrale_rectangle_python),
        ("Trapèze Python", integrale_trapeze_python),
        ("Rectangle NumPy", integrale_rectangle_numpy),
        ("Trapèze NumPy", integrale_trapeze_numpy)
    ]

    results = []

    for name, method in methods:
        start = time.perf_counter()
        I = method(a, b, p1, p2, p3, p4, n)
        end = time.perf_counter()
        error = abs(I - I_exact)
        duration = end - start
        results.append((name, I, error, duration))

    df = pd.DataFrame(results, columns=["Méthode", "Valeur Approchée", "Erreur Absolue", "Temps (s)"])
    df = df.sort_values("Erreur Absolue")
    print(df.to_string(index=False))

    # === Convergence (erreur vs n) ===
    n_values = [10, 20, 40, 80, 160, 320, 640, 1280]
    errors_rectangle_python = []
    errors_rectangle_numpy = []
    errors_trapeze_python = []
    errors_trapeze_numpy = []

    for n in n_values:
        I_rect_py = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
        I_rect_np = integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)
        I_trap_py = integrale_trapeze_python(a, b, p1, p2, p3, p4, n)
        I_trap_np = integrale_trapeze_numpy(a, b, p1, p2, p3, p4, n)

        errors_rectangle_python.append(abs(I_rect_py - I_exact))
        errors_rectangle_numpy.append(abs(I_rect_np - I_exact))
        errors_trapeze_python.append(abs(I_trap_py - I_exact))
        errors_trapeze_numpy.append(abs(I_trap_np - I_exact))

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, errors_rectangle_python, marker='o', label='Rectangle (Python)')
    plt.plot(n_values, errors_trapeze_python, marker='s', label='Trapèze (Python)')
    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence des méthodes Python (échelle linéaire)")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, errors_rectangle_numpy, marker='o', linestyle='--', label='Rectangle (NumPy)')
    plt.plot(n_values, errors_trapeze_numpy, marker='s', linestyle='--', label='Trapèze (NumPy)')
    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence des méthodes NumPy (échelle linéaire)")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.tight_layout()
    plt.show()

    #  Temps d'exécution 
    times_rect_python = []
    times_trap_python = []
    times_rect_numpy = []
    times_trap_numpy = []

    for n in n_values:
        start = time.perf_counter()
        _ = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
        times_rect_python.append(time.perf_counter() - start)

        start = time.perf_counter()
        _ = integrale_trapeze_python(a, b, p1, p2, p3, p4, n)
        times_trap_python.append(time.perf_counter() - start)

        start = time.perf_counter()
        _ = integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)
        times_rect_numpy.append(time.perf_counter() - start)

        start = time.perf_counter()
        _ = integrale_trapeze_numpy(a, b, p1, p2, p3, p4, n)
        times_trap_numpy.append(time.perf_counter() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times_rect_python, marker='o', label='Rectangle (Python)')
    plt.plot(n_values, times_trap_python, marker='s', label='Trapèze (Python)')
    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Temps de calcul - Méthodes Python")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times_rect_numpy, marker='o', linestyle='--', label='Rectangle (NumPy)')
    plt.plot(n_values, times_trap_numpy, marker='s', linestyle='--', label='Trapèze (NumPy)')
    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Temps de calcul - Méthodes NumPy")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.tight_layout()
    plt.show()

