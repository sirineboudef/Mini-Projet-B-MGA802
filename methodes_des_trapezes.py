import numpy as np

# définition des coefficients du polynôme à 3 degrès
coeffs = [2, -3, 0, 5]

# définition des bornes de l'intervalle
a = 1
b = 4

# définition du nombre de segments
n = 100

# Fonction pour évaluer le polynôme avec python basique
def integrale_trapeze(coeffs, a, b, n):
    def polynome(x):
        return coeffs[0] * x ** 3 + coeffs[1] * x ** 2 + coeffs[2] * x + coeffs[3]

    h = (b - a) / n
    somme = 0
    for i in range(1, n):
        x_i = a + i * h
        somme += polynome(x_i)

    integrale = (h / 2) * (polynome(a) + 2 * somme + polynome(b))
    return integrale

# Fonction pour évaluer le polynôme avec numpy
def integrale_trapeze(coeffs, a, b, n):
    def polynome(x):
        return coeffs[0] * x ** 3 + coeffs[1] * x ** 2 + coeffs[2] * x + coeffs[3]

    x = np.linspace(a, b, n + 1)
    y = polynome(x)
    h = (b - a) / n
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

print(f"L'intégrale approchée du polynôme sur [{a}, {b}] est : {integrale:.6f}")
