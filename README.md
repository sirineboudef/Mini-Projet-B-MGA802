# Mini-Projet-B-MGA802

## Objectif : Intégration numérique d’un polynôme par différentes méthodes

Ce projet compare plusieurs méthodes d’intégration numérique, à la fois en Python de base et avec NumPy. Il inclut également une solution analytique pour évaluer l’erreur, ainsi que des analyses de convergence et de performance.

---

## Structure du projet

| Fichier                         | Description |
|--------------------------------|-------------|
| `polynome.py`                  | Définition du polynôme \( f(x) = p_1 + p_2 x + p_3 x^2 + p_4 x^3 \) |
| `methode_analytique.py`        | Calcule l'intégrale exacte de \( f(x) \) entre `a` et `b` |
| `methode_rectangle_python.py`  | Méthode des rectangles (implémentation en Python pur) |
| `Methode_rectangle_Numpy.py`   | Méthode des rectangles (implémentation vectorisée avec NumPy) |
| `methode_trapeze.py`           | Méthode des trapèzes (Python pur et NumPy) |
| `methode_de_simpson.py`        | Méthode de Simpson (Python pur et NumPy) |
| `main.py`                      | Compare toutes les méthodes, calcule les erreurs, temps et génère les graphiques |

---

## Comment exécuter

### Pour tester **une seule méthode**
Tu peux exécuter n’importe lequel des modules (`methode_rectangle_python.py`, `methode_trapeze.py`, etc.) pour afficher :

- La valeur approchée
- L’erreur absolue
- Le temps d’exécution
- La convergence (pour certains modules)

### Pour tester **tout le projet d’un coup**
Lance simplement :

```bash
python main.py
