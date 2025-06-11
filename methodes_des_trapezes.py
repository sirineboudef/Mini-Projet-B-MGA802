import numpy as np
from  methode_rectangle_python import*
import time
import matplotlib.pyplot as plt
from Methode_rectangle_Numpy import*
from methode_trapeze_scipy import*

# définition des coefficients du polynôme à 3 degrès
coeffs = [26, 36, 12, 7]

# valeur fixe pour le coefficient du polynome et limites d'intégration

a, b = -50, 50  # bornes de l'intégrale
n = 10  # nombre de segments pour la méthode des rectangles

# fonction pour évaluer le polynôme avec python basique
def integrale_trapeze_python(coeffs, a, b, n):
    def polynome(x):
        return coeffs[0] * x ** 3 + coeffs[1] * x ** 2 + coeffs[2] * x + coeffs[3]

    h = (b - a) / n
    somme = 0
    for i in range(1, n):
        x_i = a + i * h
        somme += polynome(x_i)

    integrale = (h / 2) * (polynome(a) + 2 * somme + polynome(b))
    return integrale

# fonction pour évaluer le polynôme avec numpy
def integrale_trapeze_numpy(coeffs, a, b, n):
    def polynome(x):
        return coeffs[0] * x ** 3 + coeffs[1] * x ** 2 + coeffs[2] * x + coeffs[3]

    x = np.linspace(a, b, n + 1)
    y = polynome(x)
    h = (b - a) / n
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

# affichage d’un premier résultat
resultat = integrale_trapeze_python(coeffs, a, b, n)
print(f"L'intégrale approchée du polynôme sur [{a}, {b}] est : {resultat:.6f}")

#defintion de la méthode de comparaison
def comparer_methodes(coeffs, a, b, n):
    # Calcul du temps d'execution de la methodes trapèzes avec python de base
    debut_trapeze_python = time.time()
    resultat_trapeze_python = integrale_trapeze_python(coeffs, a, b, n)
    fin_trapeze_python = time.time()

    # Calcul du temps d'execution de la methodes trapèzes avec numpy
    debut_trapeze_numpy = time.time()
    resultat_trapeze_numpy = integrale_trapeze_numpy(coeffs, a, b, n)
    fin_trapeze_numpy = time.time()

    # Calcul du temps d'execution de la methode trapèzes avec SciPy
    debut_trapeze_scipy = time.time()
    resultat_trapeze_scipy = integrale_trapeze_scipy(a, b,coeffs[0],coeffs[1],coeffs[2],coeffs[3],  n)
    fin_trapeze_scipy = time.time()

    # Calcul du temps d'execution de la methodes des rectangles avec python de base
    debut_rectangle_python = time.time()
    resultat_rectangle_python = integrale_rectangle_python(coeffs, a, b, n)
    fin_rectangle_python = time.time()

    # Calcul du temps d'execution de la methodes des rectangles avec numpy
    debut_rectangle_numpy = time.time()
    resultat_rectangle_numpy = integrale_rectangle_numpy(coeffs, a, b, n)
    fin_rectangle_numpy = time.time()

    # calcul de la valeur exacte de l'integral
    resultat_exact = integrale_analytique(a, b, 26, 36, 12, 7)

    # calcul des erreurs de differentes methodes
    erreur_trapeze_python = abs(resultat_trapeze_python - resultat_exact)
    erreur_trapeze_numpy = abs(resultat_trapeze_numpy - resultat_exact)
    erreur_trapeze_scipy = abs(resultat_trapeze_scipy - resultat_exact)
    erreur_rectangle_python = abs(resultat_rectangle_python - resultat_exact)
    erreur_rectangle_numpy = abs(resultat_rectangle_numpy - resultat_exact)

    # Affichage des resultats
    print("\n--- Comparaison des méthodes ---")
    print(f"Trapèzes (python de base)       : Résultat = {resultat_trapeze_python:.6f}, Erreur = {erreur_trapeze_python:.2e}, Temps = {fin_trapeze_python - debut_trapeze_python:.6f} s")
    print(f"Trapèzes (numpy)                : Résultat = {resultat_trapeze_numpy:.6f}, Erreur = {erreur_trapeze_numpy:.2e}, Temps = {fin_trapeze_numpy - debut_trapeze_numpy:.6f} s")
    print(f"Trapèzes (scipy)                : Résultat = {resultat_trapeze_scipy:.6f}, Erreur = {erreur_trapeze_scipy:.2e}, Temps = {fin_trapeze_scipy - debut_trapeze_scipy:.6f} s")
    print(f"Rectangles (python de base)     : Résultat = {resultat_rectangle_python:.6f}, Erreur = {erreur_rectangle_python:.2e}, Temps = {fin_rectangle_python - debut_rectangle_python:.6f} s")
    print(f"Rectangles (numpy)              : Résultat = {resultat_rectangle_numpy:.6f}, Erreur = {erreur_rectangle_numpy:.2e}, Temps = {fin_rectangle_numpy - debut_rectangle_numpy:.6f} s")
    print(f"Valeur exacte                   : {resultat_exact:.6f}")

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
