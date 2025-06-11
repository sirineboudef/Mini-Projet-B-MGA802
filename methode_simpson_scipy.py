from scipy.integrate import simpson
from polynome import f
import numpy as np

def integrale_simpson_scipy(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode de Simpson sur n segments. Version pré-programmée SciPy"""
    x = np.linspace(a, b, n)
    y = f(x, p1, p2, p3, p4)
    return simpson(y,x=x)

# -------------- Test du module --------------

# Valeurs fixes pour les coefficients du polynome et limites d'intégration
# p1, p2, p3, p4 = 26, 36, 12, 7  # coefficients du polynôme
# a, b = -50, 50  # bornes de l'intégrale
# n = 10  # nombre de points pour les méthodes

# Test de la fonction
print(integrale_simpson_scipy(-50, 50, 26, 36, 12, 7, 1000))