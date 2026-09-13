"""
Exercice 1.4 : Générer 1000 entiers aléatoires entre 0 et 100,
puis compter le nombre d'occurrences de chaque valeur.
"""
import random
from collections import Counter

# Génération de la liste de 1000 nombres aléatoires
nombres = [random.randint(0, 100) for _ in range(1000)]

# Comptage des occurrences avec Counter (module standard)
occurrences = Counter(nombres)

# Affichage trié par valeur (de 0 à 100)
print("Valeur : Nombre d'occurrences")
for valeur in sorted(occurrences):
    print(f"{valeur:3d} : {occurrences[valeur]}")

print(f"\nNombre de valeurs distinctes : {len(occurrences)}")
print(f"Valeur la plus fréquente : {occurrences.most_common(1)[0]}")

# Version sans utiliser Counter, avec un dictionnaire simple
def compter_occurrences_manuel(liste):
    resultat = {}
    for x in liste:
        resultat[x] = resultat.get(x, 0) + 1
    return resultat

occurrences_manuel = compter_occurrences_manuel(nombres)
assert occurrences_manuel == dict(occurrences)  # vérification de cohérence
print("\nVérification : le comptage manuel correspond au Counter -> OK")
