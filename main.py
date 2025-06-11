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
from methode_trapeze import integrale_trapeze_python, integrale_trapeze_numpy
from methode_de_simpson import integrale_simpson_python, integrale_simpson_numpy
# Définition des coefficients du polynôme
p1, p2, p3, p4 = 26, 36, 12, 7

# Version vectorisée pour NumPy
def f_vectorized(x):
    return p1 + p2 * x + p3 * x**2 + p4 * x**3

# Paramètres d'intégration
a, b = -50, 50
n = 10

# Resultats de toutes les methodes avec erreur et temps d'execution
methods = [
    ("Rectangle Python", integrale_rectangle_python),
    ("Simpson Python", integrale_simpson_python),
    ("Trapeze Python", integrale_trapeze_python),
    ("Rectangle NumPy", integrale_rectangle_numpy),
    ("Simpson NumPy", integrale_simpson_numpy),
    ("Trapeze NumPy", integrale_trapeze_numpy),
]

I_exact = integrale_analytique(a, b, p1, p2, p3, p4)
results = []
print("=== Resultats de toutes les methodes ===")
# Boucle pour calculer les resultats de toutes les methodes
for name, method in methods:
    start = time.perf_counter()
    I = method(a, b, p1, p2, p3, p4, n)
    end = time.perf_counter()
    error = abs(I - I_exact)
    duration = end - start
    results.append((name, I, error, duration))
    print(f"{name:<20} → I = {I:.6f}, erreur = {error:.3e}, durée = {duration:.10f}s")

# Generation des graphiques d'erreur en fonction du nombre de segments
# Version de python de base
n_values = [10, 20, 40, 80, 160, 320, 640, 1280] # Valeurs de n à tester
# Listes d’erreurs
errors_rectangle = []
errors_simpson = []
errors_trapeze = []

# Calcul de la valeur exacte de l'integrale
I_exact = integrale_analytique(a, b, p1, p2, p3, p4)

# Calcul des erreurs pour chaque méthode et chaque segment
for n in n_values:
    I_rect = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
    I_simp = integrale_simpson_python(a, b, p1, p2, p3, p4, n)
    I_trap = integrale_trapeze_python (a, b, p1, p2, p3, p4, n)
    err_rect = abs(I_rect - I_exact)
    err_simp = abs(I_simp - I_exact)
    err_trap = abs(I_trap - I_exact)
    errors_rectangle.append(err_rect)
    errors_simpson.append(err_simp)
    errors_trapeze.append(err_trap)

# Tracé des graphiques avec échelle linéaire
plt.figure(figsize=(8, 5))
plt.plot(n_values, errors_rectangle, marker='o', label='Rectangle (Python)')
plt.plot(n_values, errors_simpson, marker='s', label='Simpson (Python)')
plt.plot(n_values, errors_trapeze, marker='x', label='Trapeze (Python)')
plt.xlabel("Nombre de segments (n)")
plt.ylabel("Erreur absolue")
plt.title("Convergence des méthodes numériques (échelle linéaire)")
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

# Version de numpy
# liste des erreurs
errors_rectangle_numpy = []
errors_simpson_numpy = []
errors_trapeze_numpy = []

# Calcul des erreurs pour chaque méthode et chaque segment
for n in n_values:
    I_rect_np = integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)
    I_simp_np = integrale_simpson_numpy(a, b, p1, p2, p3, p4, n)
    I_trap_np = integrale_trapeze_numpy(a, b, p1, p2, p3, p4, n)

    err_rect_np = abs(I_rect_np - I_exact)
    err_simp_np = abs(I_simp_np - I_exact)
    err_trap_np = abs(I_trap_np - I_exact)

    errors_rectangle_numpy.append(err_rect_np)
    errors_simpson_numpy.append(err_simp_np)
    errors_trapeze_numpy.append(err_trap_np)

# Affichage du graphique NumPy (échelle linéaire)
plt.figure(figsize=(8, 5))
plt.plot(n_values, errors_rectangle_numpy, marker='o', label='Rectangle (NumPy)')
plt.plot(n_values, errors_simpson_numpy, marker='s', label='Simpson (NumPy)')
plt.plot(n_values, errors_trapeze_numpy, marker='x', label='Trapeze (NumPy)')
plt.xlabel("Nombre de segments (n)")
plt.ylabel("Erreur absolue")
plt.title("Convergence des méthodes numériques avec NumPy (échelle linéaire)")
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

# graphiques du temps d'execution en fonction du nombre de segments
# version python de base

# Valeurs de n à tester
n_values = [10, 50, 100, 200, 400, 800, 1600, 3200]

# Listes pour stocker les temps
times_rectangle_python = []
times_rectangle_numpy = []
times_simpson_python = []
times_simpson_numpy = []
times_trapeze_python = []
times_trapeze_numpy = []

# Boucle de mesure du temps
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

    # Trapeze Python
    start_sp = time.perf_counter()
    integrale_trapeze_python(a, b, p1, p2, p3, p4, n)
    end_sp = time.perf_counter()
    times_trapeze_python.append(end_sp - start_sp)

    # Trapeze NumPy
    start_sn = time.perf_counter()
    integrale_trapeze_numpy(a, b, p1, p2, p3, p4, n)
    end_sn = time.perf_counter()
    times_trapeze_numpy.append(end_sn - start_sn)

# Tracé du graphique de comparaison des temps
plt.figure(figsize=(10, 6))

plt.plot(n_values, times_rectangle_python, marker='o', label="Rectangle (Python)")
plt.plot(n_values, times_rectangle_numpy, marker='o', linestyle='--', label="Rectangle (NumPy)")
plt.plot(n_values, times_simpson_python, marker='s', label="Simpson (Python)")
plt.plot(n_values, times_simpson_numpy, marker='s', linestyle='--', label="Simpson (NumPy)")
plt.plot(n_values, times_trapeze_python, marker='x', label="Trapeze (Python)")
plt.plot(n_values, times_trapeze_numpy, marker='x', linestyle='--', label="Trapeze (NumPy)")
plt.xlabel("Nombre de segments (n)")
plt.ylabel("Temps d'exécution (secondes)")
plt.title("Temps de calcul des méthodes numériques (Rectangle & Simpson)")
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

# Creation d'un Histogramme des erreurs absolues pour chaque méthode pour comparaison de precision
import matplotlib.pyplot as plt

# Recuperation des resultats (nom, valeur approximative, erreur, durée)
method_names = [r[0] for r in results]
erreurs = [r[2] for r in results]

# Couleurs differente pour chaque méthode
colors = plt.cm.tab10.colors[:len(method_names)]  # maximum de 10 couleurs distinctes

# Tracer l’histogramme
plt.figure(figsize=(10, 6))
barres = plt.bar(method_names, erreurs, color=colors)

# Ajout de la valeur de l’erreur sur chaque barre
for bar, err in zip(barres, erreurs):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             f"{err:.2e}", ha='center', va='bottom', fontsize=10)

plt.ylabel("Erreur absolue")
plt.title("Comparaison des méthodes – Erreur absolue")
plt.xticks(rotation=30)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

