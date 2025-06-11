"""
main.py
-------
Ce script est le code principal du projet d'intégration numérique.

Il permet de comparer différentes méthodes d'intégration :
1- Méthodes écrites avec Python pur (Rectangle, Trapèze, Simpson)
2- Méthodes vectorisées avec NumPy
3- Méthodes utilisant les fonctions intégrées de SciPy

Les résultats obtenus incluent :
1- La valeur approchée de l'intégrale d'un polynôme sur un intervalle donné
2- L'erreur absolue par rapport à l'intégrale analytique
3- Le temps d'exécution de chaque méthode

L'utilisateur peut aussi exécuter individuellement chaque module (méthode) pour répondre aux questions de chaque partie.

Auteur : Syrine Boudef-Wilson Parra-Linda Ghazouani-Paulin Muhlhoff
Projet : Mini-Projet B - MGA802
Date : Juin 2025
"""

# importations necessaire
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
from polynome import f
from methode_analytique import integrale_analytique
from methode_rectangle_python import integrale_rectangle_python
from Methode_rectangle_Numpy import integrale_rectangle_numpy
from methode_trapeze import integrale_trapeze_python, integrale_trapeze_numpy
from methode_de_simpson import integrale_simpson_python, integrale_simpson_numpy
from methode_simpson_scipy import integrale_simpson_scipy

# Définition des coefficients du polynôme
p1, p2, p3, p4 = 26, 36, 12, 7

# Paramètres d'intégration
a, b = -50, 50
n = 10

# Liste des méthodes à tester
methods = [
    ("Rectangle Python", integrale_rectangle_python),
    ("Simpson Python", integrale_simpson_python),
    ("Trapeze Python", integrale_trapeze_python),
    ("Rectangle NumPy", integrale_rectangle_numpy),
    ("Simpson NumPy", integrale_simpson_numpy),
    ("Trapeze NumPy", integrale_trapeze_numpy),
    ("Simpson SciPy", integrale_simpson_scipy)
]

# Calcul de la valeur exacte
I_exact = integrale_analytique(a, b, p1, p2, p3, p4)
results = []

print("\n=== Résultats de toutes les méthodes ===")
for name, method in methods:
    start = time.perf_counter()
    I = method(a, b, p1, p2, p3, p4, n)
    end = time.perf_counter()
    error = abs(I - I_exact)
    duration = end - start
    results.append((name, I, error, duration))
    print(f"{name:<20} → I = {I:.6f}, erreur = {error:.3e}, durée = {duration:.10f}s")

# Histogramme des erreurs absolues
method_names = [r[0] for r in results]
errors = [r[2] for r in results]
colors = plt.cm.tab10.colors[:len(method_names)]

plt.figure(figsize=(10, 6))
bars = plt.bar(method_names, errors, color=colors)
for bar, err in zip(bars, errors):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             f"{err:.2e}", ha='center', va='bottom', fontsize=10)

plt.ylabel("Erreur absolue")
plt.title("Comparaison des méthodes – Erreur absolue")
plt.xticks(rotation=30)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
