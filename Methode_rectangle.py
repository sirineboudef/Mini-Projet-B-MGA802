def f(x: float, p1: float, p2: float, p3: float, p4: float):
    """Fonction polynomiale du troisième degré."""
    return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3

def integral_analytique(a: float, b: float, p1: float, p2: float, p3: float, p4: float):
    """Intégrale analytique de f(x) entre a et b"""
    term1 = p1 * (b - a)
    term2 = p2 * (b ** 2 - a ** 2) / 2
    term3 = p3 * (b ** 3 - a ** 3) / 3
    term4 = p4 * (b ** 4 - a ** 4) / 4
    return term1 + term2 + term3 + term4

def integral_rectangle(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    """Intégration numérique par la méthode des rectangles sur n segments."""
    h = (b - a) / n  # largeur d'un segment
    total = 0
    x = a
    for _ in range(n):
        total += f(x, p1, p2, p3, p4) * h
        x += h
    return total







