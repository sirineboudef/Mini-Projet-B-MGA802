import numpy as np
import time
import matplotlib.pyplot as plt

from scipy.integrate import trapezoid

from Methode_rectangle_Numpy import*
from  methode_rectangle_python import*
from polynome import f
from methode_rectangle_python import*
from methodes_des_trapezes import *


def integrale_trapeze_scipy(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode des trapèzes sur n segments. Version pré-programmée SciPy"""
    x = np.linspace(a, b, num=n)
    y = f(x, p1, p2, p3, p4)
    return trapezoid(y, x=x)

# -------------- Test du module --------------

# Valeurs fixes pour les coefficients du polynome et limites d'intégration
p1, p2, p3, p4 = 26, 36, 12, 7  # coefficients du polynôme
a, b = -50, 50  # bornes de l'intégrale
n = 10  # nombre de points pour les méthodes

# Test de la fonction
# print(integrale_trapeze_scipy(a, b, p1, p2, p3, p4, n))

# -------------- Affichage des performances de la méthode --------------
#valeurs du nombre de segments à tester
liste_nombre_segments = [10, 50, 100, 500, 1000, 1500, 2000, 2500, 5000, 10000]

# Stockage des erreurs et du temps de calcul
liste_erreurs_trapeze_python = []
liste_erreurs_trapeze_numpy = []
liste_erreurs_trapeze_scipy = []
liste_temps_trapeze_python = []
liste_temps_trapeze_numpy = []
liste_temps_trapeze_scipy = []

# Calcul de la valeur exacte de l'intégrale
valeur_integrale_exacte = integrale_analytique(a, b, 26, 36, 12, 7)

#évaluation
for nombre_segments in liste_nombre_segments:
    #méthode trapèze avec python
    debut_temps_python = time.time()
    valeur_approchee_python = integrale_trapeze_python(coeffs, a, b, nombre_segments)
    fin_temps_python = time.time()
    temps_execution_python = fin_temps_python - debut_temps_python
    erreur_python = abs(valeur_approchee_python - valeur_integrale_exacte)

    liste_temps_trapeze_python.append(temps_execution_python)
    liste_erreurs_trapeze_python.append(erreur_python)

    #méthode trapèze avec numpy
    debut_temps_numpy = time.time()
    valeur_approchee_numpy = integrale_trapeze_numpy(coeffs, a, b, nombre_segments)
    fin_temps_numpy = time.time()
    temps_execution_numpy = fin_temps_numpy - debut_temps_numpy
    erreur_numpy = abs(valeur_approchee_numpy - valeur_integrale_exacte)

    liste_temps_trapeze_numpy.append(temps_execution_numpy)
    liste_erreurs_trapeze_numpy.append(erreur_numpy)

    #méthode trapèze avec scipy
    debut_temps_scipy = time.time()
    valeur_approchee_scipy = integrale_trapeze_scipy(a, b,coeffs[0],coeffs[1],coeffs[2],coeffs[3], nombre_segments)
    fin_temps_scipy = time.time()
    temps_execution_scipy = fin_temps_scipy - debut_temps_scipy
    erreur_scipy = abs(valeur_approchee_scipy - valeur_integrale_exacte)

    liste_temps_trapeze_scipy.append(temps_execution_scipy)
    liste_erreurs_trapeze_scipy.append(erreur_scipy)


#génération du graphique de convergence
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
plt.show()

#génération du graphique des temps de calcul
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
plt.show()