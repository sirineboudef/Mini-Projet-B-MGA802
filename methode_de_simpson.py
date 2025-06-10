import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from methode_rectangle_python import integrale_rectangle_python
from Methode_rectangle_Numpy import integrale_rectangle_numpy
from methode_analytique import integrale_analytique
from polynome import f  # Fonction scalaire importée

# Définition des coefficients du polynôme
p1, p2, p3, p4 = 26, 36, 12, 7

# Version vectorisée pour NumPy
def f_vectorized(x):
    return p1 + p2 * x + p3 * x**2 + p4 * x**3

# Méthode de Simpson avec Python pur
def integrale_simpson_python(a, b, p1, p2, p3, p4, n=10):
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    total = f(a, p1, p2, p3, p4) + f(b, p1, p2, p3, p4)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            total += 2 * f(x, p1, p2, p3, p4)
        else:
            total += 4 * f(x, p1, p2, p3, p4)
    return (h / 3) * total

# Méthode de Simpson avec NumPy
def integrale_simpson_numpy(a, b, p1, p2, p3, p4, n=10):
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f_vectorized(x)
    coeffs = np.ones(n + 1)
    coeffs[1:-1:2] = 4
    coeffs[2:-1:2] = 2
    return (h / 3) * np.sum(coeffs * y)

# Paramètres d'intégration
a, b = -50, 50
n = 10

# Calculs directs
resultat_python = integrale_simpson_python(a, b, p1, p2, p3, p4, n)
resultat_numpy = integrale_simpson_numpy(a, b, p1, p2, p3, p4, n)

print(f"Résultat avec Simpson Python: {resultat_python:.6f}")
print(f"Résultat avec Simpson NumPy : {resultat_numpy:.6f}")

# 2eme question: Comparaison de toutes les méthodes
methods = [
    ("Rectangle Python", integrale_rectangle_python),
    ("Simpson Python", integrale_simpson_python),
    ("Rectangle NumPy", integrale_rectangle_numpy),
    ("Simpson NumPy", integrale_simpson_numpy),
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

# Convergence des méthodes NumPy
n_values = [10, 20, 40, 80, 160, 320, 640, 1280]

errors_rectangle_numpy = []
errors_simpson_numpy = []

for n in n_values:
    I_rect_np = integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)
    I_simp_np = integrale_simpson_numpy(a, b, p1, p2, p3, p4, n)

    err_rect_np = abs(I_rect_np - I_exact)
    err_simp_np = abs(I_simp_np - I_exact)

    errors_rectangle_numpy.append(err_rect_np)
    errors_simpson_numpy.append(err_simp_np)

# Affichage du graphique NumPy (échelle linéaire)
plt.figure(figsize=(8, 5))
plt.plot(n_values, errors_rectangle_numpy, marker='o', label='Rectangle (NumPy)')
plt.plot(n_values, errors_simpson_numpy, marker='s', label='Simpson (NumPy)')
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

# Tracé du graphique de comparaison des temps
plt.figure(figsize=(10, 6))

plt.plot(n_values, times_rectangle_python, marker='o', label="Rectangle (Python)")
plt.plot(n_values, times_rectangle_numpy, marker='o', linestyle='--', label="Rectangle (NumPy)")
plt.plot(n_values, times_simpson_python, marker='s', label="Simpson (Python)")
plt.plot(n_values, times_simpson_numpy, marker='s', linestyle='--', label="Simpson (NumPy)")

plt.xlabel("Nombre de segments (n)")
plt.ylabel("Temps d'exécution (secondes)")
plt.title("Temps de calcul des méthodes numériques (Rectangle & Simpson)")
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()
