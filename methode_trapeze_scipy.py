import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid
from methode_trapeze import integrale_trapeze_python, integrale_trapeze_numpy
from methode_analytique import integrale_analytique
from polynome import f

# --- Paramètres globaux ---
p1, p2, p3, p4 = 26, 36, 12, 7  # Coefficients du polynôme
a, b = -50, 50                  # Bornes de l'intégration
n = 10                          # Nombre de points

# --- Fonction principale : intégrale avec trapèze SciPy ---
def integrale_trapeze_scipy(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode des trapèzes sur n segments (avec SciPy)"""
    x = np.linspace(a, b, num=n)
    y = f(x, p1, p2, p3, p4)
    return trapezoid(y, x=x)


# -------------------- TEST ET VISUALISATION --------------------

# Valeurs du nombre de segments à tester
liste_nombre_segments = [10, 50, 100, 500, 1000, 1500, 2000, 2500, 5000, 10000]

# Stockage des erreurs et du temps de calcul
liste_erreurs_trapeze_python = []
liste_erreurs_trapeze_numpy = []
liste_erreurs_trapeze_scipy = []
liste_temps_trapeze_python = []
liste_temps_trapeze_numpy = []
liste_temps_trapeze_scipy = []

# Valeur de référence (intégrale exacte)
valeur_integrale_exacte = integrale_analytique(a, b, p1, p2, p3, p4)

for n in liste_nombre_segments:
    # Trapèze Python
    t0 = time.perf_counter()
    val_py = integrale_trapeze_python(a, b, p1, p2, p3, p4, n)
    t1 = time.perf_counter()
    err_py = abs(val_py - valeur_integrale_exacte)
    liste_erreurs_trapeze_python.append(err_py)
    liste_temps_trapeze_python.append(t1 - t0)

    # Trapèze NumPy
    t0 = time.perf_counter()
    val_np = integrale_trapeze_numpy(a, b, p1, p2, p3, p4, n)
    t1 = time.perf_counter()
    err_np = abs(val_np - valeur_integrale_exacte)
    liste_erreurs_trapeze_numpy.append(err_np)
    liste_temps_trapeze_numpy.append(t1 - t0)

    # Trapèze SciPy
    t0 = time.perf_counter()
    val_sp = integrale_trapeze_scipy(a, b, p1, p2, p3, p4, n)
    t1 = time.perf_counter()
    err_sp = abs(val_sp - valeur_integrale_exacte)
    liste_erreurs_trapeze_scipy.append(err_sp)
    liste_temps_trapeze_scipy.append(t1 - t0)

# --- Graphique : Erreur (log-log) ---
plt.figure()
plt.plot(liste_nombre_segments, liste_erreurs_trapeze_python, label="Trapèze Python (erreur)")
plt.plot(liste_nombre_segments, liste_erreurs_trapeze_numpy, label="Trapèze NumPy (erreur)")
plt.plot(liste_nombre_segments, liste_erreurs_trapeze_scipy, label="Trapèze SciPy (erreur)")
plt.xlabel("Nombre de segments")
plt.ylabel("Erreur absolue")
plt.title("Convergence de la méthode des trapèzes")
plt.legend()
plt.grid(True)
plt.xscale("log")
plt.yscale("log")
plt.tight_layout()
plt.show()

# --- Graphique : Temps d'exécution (log-log) ---
plt.figure()
plt.plot(liste_nombre_segments, liste_temps_trapeze_python, label="Trapèze Python (temps)")
plt.plot(liste_nombre_segments, liste_temps_trapeze_numpy, label="Trapèze NumPy (temps)")
plt.plot(liste_nombre_segments, liste_temps_trapeze_scipy, label="Trapèze SciPy (temps)")
plt.xlabel("Nombre de segments")
plt.ylabel("Temps de calcul (secondes)")
plt.title("Temps d'exécution de la méthode des trapèzes")
plt.legend()
plt.grid(True)
plt.xscale("log")
plt.yscale("log")
plt.tight_layout()
plt.show()
