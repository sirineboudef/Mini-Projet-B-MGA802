import numpy as np

# Definition du polynome du 3eme degre a integrer

def f(x: float, p1: float, p2: float, p3: float, p4: float):
    return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3

# Fonction polynomiale vectorisée
def f_vect(x: np.ndarray, p1: float, p2: float, p3: float, p4: float) -> np.ndarray:
    """Fonction polynomiale du 3e degré (vectorisée)"""
    return p1 + p2 * x + p3 * x**2 + p4 * x**3