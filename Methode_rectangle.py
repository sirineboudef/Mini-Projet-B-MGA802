# Importations des modules et packages necessaires
import timeit
from methode_analytique import integrale_analytique
from methode_de_rectangle import integrale_rectangle_python
from polynome import f

# Fonction d'integration par la methode des rectangles
def integrale_rectangle_python(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):
    pas = (b - a) / n  # largeur d'un segment
    valeure_integrale = 0
    for i in range(n):
        x = a + (i + 0.5) * pas  # Point du milieu
        valeure_integrale += f(x, p1, p2, p3, p4)
    return pas * valeure_integrale

# Fonction pour calculer l'erreur absolu de l'integration
def erreur_integration(a: float, b: float, p1: float, p2: float, p3: float, p4: float, n: int = 10):

    exact = integrale_analytique(a, b, p1, p2, p3, p4)
    approx = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
    return abs(exact - approx)

# Fonction pour tester la convergence du resultats en fonction du nombre de segments
def tester_convergence(a: float, b: float, p1: float, p2: float, p3: float, p4: float):
    """Affiche l'erreur pour des valeurs croissantes de n."""
    print("\nTest de convergence :")
    for n in [10, 100, 1000, 10000, 100000]:
        err = erreur_integration(a, b, p1, p2, p3, p4, n)
        print(f"n={n:<7} erreur={err:.10f}")

# Fontion pour la mesure du temps d'execution de l'integration
def mesurer_temps_execution(a, b, p1, p2, p3, p4, n):
    temps = timeit.timeit(lambda: integrale_rectangle_python(a, b, p1, p2, p3, p4, n), number=1)
    print(f"\nTemps d'exécution pour n={n} : {temps:.6f} secondes")


# valeur fixe pour le coefficient du polynome et limites d'intégration
p1, p2, p3, p4 = 26, 36, 12, 7  # coefficients du polynôme
a, b = -50, 50  # bornes de l'intégrale
n = 10  # nombre de segments pour la méthode des rectangles

# Tester les resultats

valeur_exacte = integrale_analytique(a, b, p1, p2, p3, p4)
valeur_approx = integrale_rectangle_python(a, b, p1, p2, p3, p4, n)
erreur = erreur_integration(a, b, p1, p2, p3, p4, n)

print(f"Intégrale analytique   : {valeur_exacte}")
print(f"Intégrale numérique    : {valeur_approx}")
print(f"Erreur absolue (n={n}): {erreur}")

tester_convergence(a, b, p1, p2, p3, p4)
mesurer_temps_execution(a, b, p1, p2, p3, p4, n)









