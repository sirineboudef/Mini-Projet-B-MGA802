import numpy as np
import time
import pandas as pd
from scipy.integrate import simpson

from methode_analytique import integrale_analytique
from methode_de_simpson import *
from polynome import f  # Fonction scalaire importée



def integrale_simpson_scipy(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode de Simpson sur n segments. Version pré-programmée SciPy"""
    x = np.linspace(a, b, n)
    y = f(x, p1, p2, p3, p4)
    return simpson(y,x=x)

# -------------- Test du module --------------

# Valeurs fixes pour les coefficients du polynome et limites d'intégration
p1, p2, p3, p4 = 26, 36, 12, 7  # coefficients du polynôme
a, b = -50, 50  # bornes de l'intégrale
n = 10  # nombre de points pour les méthodes

# Test de la fonction
print(integrale_simpson_scipy(-50, 50, 26, 36, 12, 7, 1000))

# -------------- Affichage des performances de la méthode --------------

# Calculs directs
resultat_python = integrale_simpson_python(a, b, p1, p2, p3, p4, n)
resultat_numpy = integrale_simpson_numpy(a, b, p1, p2, p3, p4, n)
resultat_scipy = integrale_simpson_scipy(a, b, p1, p2, p3, p4, n)

print(f"Résultat avec Simpson Python: {resultat_python:.6f}")
print(f"Résultat avec Simpson NumPy : {resultat_numpy:.6f}")
print(f"Résultat avec Simpson SciPy : {resultat_scipy:.6f}")

# 2eme question: Comparaison de toutes les méthodes
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

# 3eme question : graphiques


# Valeurs de n à tester
n_values = [10, 20, 40, 80, 160, 320, 640, 1280]

# Listes d’erreurs
errors_rectangle = []
errors_simpson = []

# Valeur exacte
I_exact = integrale_analytique(a, b, p1, p2, p3, p4)

# Calcul des erreurs pour chaque méthode et chaque n
for n in n_values:
    I_rect = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
    I_simp = integrale_simpson_python(a, b, p1, p2, p3, p4, n)

    err_rect = abs(I_rect - I_exact)
    err_simp = abs(I_simp - I_exact)

    errors_rectangle.append(err_rect)
    errors_simpson.append(err_simp)

# Tracé avec échelle linéaire
plt.figure(figsize=(8, 5))
plt.plot(n_values, errors_rectangle, marker='o', label='Rectangle (Python)')
plt.plot(n_values, errors_simpson, marker='s', label='Simpson (Python)')
plt.xlabel("Nombre de segments (n)")
plt.ylabel("Erreur absolue")
plt.title("Convergence des méthodes numériques (échelle linéaire)")
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

# Convergence des méthodes NumPy et de la méthode Simpson SciPy
n_values = [10, 20, 40, 80, 160, 320, 640, 1280]

errors_rectangle_numpy = []
errors_simpson_numpy = []
errors_simpson_scipy = []

for n in n_values:
    I_rect_np = integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)
    I_simp_np = integrale_simpson_numpy(a, b, p1, p2, p3, p4, n)
    I_simp_sp = integrale_simpson_scipy(a, b, p1, p2, p3, p4, n)

    err_rect_np = abs(I_rect_np - I_exact)
    err_simp_np = abs(I_simp_np - I_exact)
    err_simp_sp = abs(I_simp_sp - I_exact)

    errors_rectangle_numpy.append(err_rect_np)
    errors_simpson_numpy.append(err_simp_np)
    errors_simpson_scipy.append(err_simp_sp)

# Affichage du graphique NumPy (échelle linéaire)
plt.figure(figsize=(8, 5))
plt.plot(n_values, errors_rectangle_numpy, marker='o', label='Rectangle (NumPy)')
plt.plot(n_values, errors_simpson_numpy, marker='s', label='Simpson (NumPy)')
plt.plot(n_values, errors_simpson_scipy, marker='s', linestyle=':', label='Simpson (SciPy)')
plt.xlabel("Nombre de segments (n)")
plt.ylabel("Erreur absolue")
plt.title("Convergence des méthodes numériques avec NumPy (échelle linéaire)")
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

# 4eme question
# Valeurs de n à tester
n_values = [10, 50, 100, 200, 400, 800, 1600, 3200]

# Listes pour stocker les temps
times_rectangle_python = []
times_rectangle_numpy = []
times_simpson_python = []
times_simpson_numpy = []
times_simpson_scipy = []

# Boucle de mesure
for n in n_values:
    # Rectangle Python
    start_rp = time.perf_counter()
    integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
    end_rp = time.perf_counter()
    times_rectangle_python.append(end_rp - start_rp)

    # Rectangle NumPy
    start_rn = time.perf_counter()
    integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)
    end_rn = time.perf_counter()
    times_rectangle_numpy.append(end_rn - start_rn)

    # Simpson Python
    start_sp = time.perf_counter()
    integrale_simpson_python(a, b, p1, p2, p3, p4, n)
    end_sp = time.perf_counter()
    times_simpson_python.append(end_sp - start_sp)

    # Simpson NumPy
    start_sn = time.perf_counter()
    integrale_simpson_numpy(a, b, p1, p2, p3, p4, n)
    end_sn = time.perf_counter()
    times_simpson_numpy.append(end_sn - start_sn)

    # Simpson SciPy
    start_ss = time.perf_counter()
    integrale_simpson_scipy(a, b, p1, p2, p3, p4, n)
    end_ss = time.perf_counter()
    times_simpson_scipy.append(end_ss - start_ss)

# Tracé du graphique de comparaison des temps
plt.figure(figsize=(10, 6))

plt.plot(n_values, times_rectangle_python, marker='o', label="Rectangle (Python)")
plt.plot(n_values, times_rectangle_numpy, marker='o', linestyle='--', label="Rectangle (NumPy)")
plt.plot(n_values, times_simpson_python, marker='s', label="Simpson (Python)")
plt.plot(n_values, times_simpson_numpy, marker='s', linestyle='--', label="Simpson (NumPy)")
plt.plot(n_values, times_simpson_scipy, marker='s', linestyle=':', label="Simpson (SciPy)")


plt.xlabel("Nombre de segments (n)")
plt.ylabel("Temps d'exécution (secondes)")
plt.title("Temps de calcul des méthodes numériques (Rectangle & Simpson)")
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()
