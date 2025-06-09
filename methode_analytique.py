# Fonction d'integration analytique (Exacte) dans [a,b]
def integrale_analytique(a: float, b: float, p1: float, p2: float, p3: float, p4: float):
    term1 = p1 * (b - a)
    term2 = p2 * (b ** 2 - a ** 2) / 2
    term3 = p3 * (b ** 3 - a ** 3) / 3
    term4 = p4 * (b ** 4 - a ** 4) / 4
    return term1 + term2 + term3 + term4
