"""
Exercice 1.5 : Générer une liste de 20 nombres aléatoires.
Trier les 10 premiers en ordre croissant, les 10 derniers en ordre décroissant.
"""
import random

# Génération de la liste de 20 nombres aléatoires (entre 0 et 100)
liste = [random.randint(0, 100) for _ in range(20)]
print("Liste originale :", liste)

premiere_moitie = liste[:10]
deuxieme_moitie = liste[10:]

premiere_moitie_triee = sorted(premiere_moitie)              # croissant
deuxieme_moitie_triee = sorted(deuxieme_moitie, reverse=True)  # décroissant

resultat = premiere_moitie_triee + deuxieme_moitie_triee

print("10 premiers (croissant)  :", premiere_moitie_triee)
print("10 derniers (décroissant):", deuxieme_moitie_triee)
print("Résultat final           :", resultat)
