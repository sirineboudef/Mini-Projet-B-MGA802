# Fonction d'integration analytique (Exacte) dans [a,b]
def integrale_analytique(a: float, b: float, p1: float, p2: float, p3: float, p4: float):
    term1 = p1 * (b - a)
    term2 = p2 * (b ** 2 - a ** 2) / 2
    term3 = p3 * (b ** 3 - a ** 3) / 3
    term4 = p4 * (b ** 4 - a ** 4) / 4
    return term1 + term2 + term3 + term4

# Définition des coefficients du polynôme
p1, p2, p3, p4 = 26, 36, 12, 7

# Fonction polynomiale
def f(x: float):
    return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3

# Paramètres d'intégration
a, b = -50, 50
n = 10

# Évaluation de l'intégrale exacte
if __name__ == "__main__":
    I_exact = integrale_analytique(a, b, p1, p2, p3, p4)
    print(f"I_exact = {I_exact}")
