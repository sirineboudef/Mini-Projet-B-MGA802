# Importations necessaires
from polynome import f  # f(x, p1, p2, p3, p4)
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt

# Coefficients du polynôme
p1, p2, p3, p4 = 26, 36, 12, 7
a, b = -50, 50
n = 10  # Nombre de segments

# Valeur exacte
from methode_analytique import integrale_analytique
I_exact = integrale_analytique(a, b, p1, p2, p3, p4)

# Méthodes
from methode_rectangle_python import integrale_rectangle_python
from Methode_rectangle_Numpy import integrale_rectangle_numpy

# Fonction pour calculer l'integrale avec la methode du trapeze avec python de base
def integrale_trapeze_python(a, b, p1, p2, p3, p4, n=10):
    pas = (b - a) / n
    total = 0.5 * (f(a, p1, p2, p3, p4) + f(b, p1, p2, p3, p4))
    for i in range(1, n):
        x = a + i * pas
        total += f(x, p1, p2, p3, p4)
    return pas * total


# Fonction pour calculer l'integrale avec la methodes des traprezes avec numpy
def integrale_trapeze_numpy(a, b, p1, p2, p3, p4, n=10):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = p1 + p2 * x + p3 * x**2 + p4 * x**3
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

# 2eme question: comparaison des erreurs et temps d'execution entre les deux methode et deux version
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

# Affichage des résultats
df = pd.DataFrame(results, columns=["Méthode", "Valeur Approchée", "Erreur Absolue", "Temps (s)"])
df = df.sort_values("Erreur Absolue")
print(df.to_string(index=False))

# 3eme question: qraphique de convergence
# Valeurs de n à tester
n_values = [10, 20, 40, 80, 160, 320, 640, 1280]

# Valeur exacte
I_exact = integrale_analytique(a, b, p1, p2, p3, p4)

# Listes d'erreurs pour les 4 méthodes
errors_rectangle_python = []
errors_rectangle_numpy = []
errors_trapeze_python = []
errors_trapeze_numpy = []

# Calcul des erreurs
for n in n_values:
    # Rectangle
    I_rect_py = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
    I_rect_np = integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)

    errors_rectangle_python.append(abs(I_rect_py - I_exact))
    errors_rectangle_numpy.append(abs(I_rect_np - I_exact))

    # Trapèze
    I_trap_py = integrale_trapeze_python(a, b, p1, p2, p3, p4, n)
    I_trap_np = integrale_trapeze_numpy(a, b, p1, p2, p3, p4, n)

    errors_trapeze_python.append(abs(I_trap_py - I_exact))
    errors_trapeze_numpy.append(abs(I_trap_np - I_exact))


# --- Graphique 1 : Rectangle & Trapèze (Python) ---
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

# --- Graphique 2 : Rectangle & Trapèze (NumPy) ---
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

# 4eme question : graphique de temps en fonctions segements
import time
import matplotlib.pyplot as plt

# Valeurs de n
n_values = [10, 20, 40, 80, 160, 320, 640, 1280]

# Listes pour les temps
times_rect_python = []
times_trap_python = []
times_rect_numpy = []
times_trap_numpy = []

# Boucle de mesure
for n in n_values:
    # Rectangle Python
    start = time.perf_counter()
    _ = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
    end = time.perf_counter()
    times_rect_python.append(end - start)

    # Trapèze Python
    start = time.perf_counter()
    _ = integrale_trapeze_python(a, b, p1, p2, p3, p4, n)
    end = time.perf_counter()
    times_trap_python.append(end - start)

    # Rectangle NumPy
    start = time.perf_counter()
    _ = integrale_rectangle_numpy(a, b, p1, p2, p3, p4, n)
    end = time.perf_counter()
    times_rect_numpy.append(end - start)

    # Trapèze NumPy
    start = time.perf_counter()
    _ = integrale_trapeze_numpy(a, b, p1, p2, p3, p4, n)
    end = time.perf_counter()
    times_trap_numpy.append(end - start)

#graphique 1 :
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

# graphique 2:
plt.figure(figsize=(10, 6))
plt.plot(n_values, times_rect_numpy, marker='o', label='Rectangle (NumPy)', linestyle='--')
plt.plot(n_values, times_trap_numpy, marker='s', label='Trapèze (NumPy)', linestyle='--')
plt.xlabel("Nombre de segments (n)")
plt.ylabel("Temps d'exécution (s)")
plt.title("Temps de calcul - Méthodes NumPy")
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

