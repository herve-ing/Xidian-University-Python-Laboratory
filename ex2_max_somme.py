"""
Exercice 2.2 : Fonction acceptant un nombre arbitraire d'entiers,
et retournant leur maximum et leur somme.
"""


def max_et_somme(*nombres: int) -> tuple:
    """Retourne (maximum, somme) des entiers passés en argument."""
    if not nombres:
        raise ValueError("Il faut fournir au moins un entier.")
    return max(nombres), sum(nombres)


if __name__ == "__main__":
    maximum, total = max_et_somme(3, 17, -5, 42, 8, 42, 0)
    print(f"Maximum : {maximum}")
    print(f"Somme   : {total}")

    # Autre exemple, avec une liste "dépaquetée"
    valeurs = [1, 2, 3, 4, 5]
    maximum, total = max_et_somme(*valeurs)
    print(f"\nAvec {valeurs} -> Maximum={maximum}, Somme={total}")
