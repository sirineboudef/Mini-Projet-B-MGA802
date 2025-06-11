from scipy.integrate import trapezoid
from polynome import f
import numpy as np

def integrale_trapeze_scipy(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode des trapèzes sur n segments. Version pré-programmée SciPy"""
    x = np.linspace(a, b, num=n)
    y = f(x, p1, p2, p3, p4)
    return trapezoid(y, x=None, dx=1.0, axis=-1)

# -------------- Test du module --------------

# Valeurs fixes pour les coefficients du polynome et limites d'intégration
p1, p2, p3, p4 = 26, 36, 12, 7  # coefficients du polynôme
a, b = -50, 50  # bornes de l'intégrale
n = 11  # nombre de points pour les méthodes

# Test de la fonction
# print(integrale_trapeze_scipy(a, b, p1, p2, p3, p4, n))