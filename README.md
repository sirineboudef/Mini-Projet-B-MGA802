# Mini-Projet-B-MGA802

## Objectif : Intégration numérique d’un polynôme par différentes méthodes

Ce projet a pour but de comparer plusieurs méthodes d’intégration numérique d'un polynome à 3 degrés, à la fois en Python de base et avec NumPy. Il inclut également une solution analytique pour évaluer l’erreur, ainsi que des analyses de convergence et des performances.

---

## Structure du projet

| Fichier                         | Description |
|--------------------------------|-------------|
| `polynome.py`                  | Définition du polynôme \( f(x) = p_1 + p_2 x + p_3 x^2 + p_4 x^3 \) |
| `methode_analytique.py`        | Calcule l'intégrale exacte de \( f(x) \) entre `a` et `b` |
| `methode_rectangle_python.py`  | Méthode des rectangles (implémentation en Python de base) |
| `Methode_rectangle_Numpy.py`   | Méthode des rectangles (implémentation vectorisée avec NumPy) |
| `methode_trapeze.py`           | Méthode des trapèzes (Python de base et NumPy) |
| `methode_de_simpson.py`        | Méthode de Simpson (Python de base et NumPy) |
| `main.py`                      | Script ptincipal qui compare toutes les méthodes, calcule les erreurs, temps et génère les graphiques |

---

## Comment exécuter

### Pour tester **une seule méthode**
Pour tester chaque méthode séparément, tu peux lançer l’un des fichiers suivants, selon la méthode que tu veux tester :

```bash
python methode_rectangle_python.py
python methode_trapeze.py
python methode_de_simpson.py
```

Chaque script va afficher :

- La valeur approchée
- L’erreur absolue
- Le temps d’exécution
- La convergence (pour certains modules)

### Pour tester **tout le projet d’un coup**
Pour exécuter une comparaison complète de toutes les méthodes avec analyse d’erreur et graphiques fait la commande suivante :

```bash
python main.py
```

Ce script regroupe l’exécution de toutes les méthodes, compare les résultats, et génère les visualisations nécessaires à l’analyse.


