import  matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapezoid, simpson
from Methode_rectangle import f



def integrate_trapezoid_built_in(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode des trapèzes sur n segments. Version pré-programmée SciPy"""
    x = np.linspace(a, b, num=n)
    y = f(x, p1, p2, p3, p4)
    return trapezoid(y, x=None, dx=1.0, axis=-1)

def integrate_simpson_built_in(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode de Simpson sur n segments. Version pré-programmée SciPy"""
    x = np.linspace(a, b, num=n)
    y = f(x, p1, p2, p3, p4)
    return simpson(y, x=None, dx=1.0, axis=-1)
# Valeurs fixes pour les coefficients du polynome et limites d'intégration
p1, p2, p3, p4 = 26, 36, 12, 7  # coefficients du polynôme
a, b = -50, 50  # bornes de l'intégrale
n = 11  # nombre de segments pour la méthode des rectangles

# Test du module
print(integrate_trapezoid_built_in(a, b, p1, p2, p3, p4, n))
print(integrate_simpson_built_in(a, b, p1, p2, p3, p4, n))

