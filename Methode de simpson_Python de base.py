# Implementation du calcul avec pyhton de base
# Définition de la fonction f(x)
def f(x, p1, p2, p3, p4):
    return p1 + p2 * x + p3 * x**2 + p4 * x**3

# Paramètres de la fonction
p1, p2, p3, p4 = 26, 36, 12, 7

# Interval d'intégration
a = -50
b = 50

# Nombre de sous-intervalles (doit être pair)
n = 10
# Definition du pas d'integration
pas = (b - a) / n

# Application de la méthode de Simpson
somme = f(a, p1, p2, p3, p4) + f(b, p1, p2, p3, p4)
for i in range(1, n):
    x = a + i * pas
    # coefficient 4 pour i impair: point milieu de chaque sous intervale
    # coefficient 2 pour i pair: point intérieur partagé entre deux paraboles
    poids_simpson = 4 if i % 2 != 0 else 2
    somme += poids_simpson * f(x, p1, p2, p3, p4)
# Calcul de l'integrale
I = pas * somme / 3
print("La valeur de l'integrale avec la methode de Simpson est : " )
print(I)
