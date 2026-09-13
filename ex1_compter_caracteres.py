"""
Exercice 2.1 : Fonction qui compte les majuscules, minuscules,
chiffres et autres caractères dans une chaîne, retournés sous forme de tuple.
"""


def compter_caracteres(chaine: str) -> tuple:
    """Retourne (nb_majuscules, nb_minuscules, nb_chiffres, nb_autres)."""
    majuscules = minuscules = chiffres = autres = 0

    for c in chaine:
        if c.isupper():
            majuscules += 1
        elif c.islower():
            minuscules += 1
        elif c.isdigit():
            chiffres += 1
        else:
            autres += 1

    return majuscules, minuscules, chiffres, autres


if __name__ == "__main__":
    texte = input("Entrez une chaîne de caractères : ")
    maj, minu, chif, aut = compter_caracteres(texte)
    print(f"Majuscules : {maj}")
    print(f"Minuscules : {minu}")
    print(f"Chiffres   : {chif}")
    print(f"Autres     : {aut}")

    # Exemple de test automatique
    exemple = "Bonjour Xidian 2024! Python est top."
    print(f"\nTest sur : {exemple!r}")
    print("Résultat  :", compter_caracteres(exemple))
