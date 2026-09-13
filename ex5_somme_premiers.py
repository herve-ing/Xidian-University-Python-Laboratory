"""
Exercice 2.5 : Calcul, à l'aide d'un générateur, de la somme des nombres
premiers compris dans un intervalle donné.
Un nombre premier est un entier > 1 divisible uniquement par 1 et lui-même.
"""


def est_premier(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def generateur_premiers(debut: int, fin: int):
    """Générateur qui produit les nombres premiers dans [debut, fin]."""
    for n in range(debut, fin + 1):
        if est_premier(n):
            yield n


def somme_premiers(debut: int, fin: int) -> int:
    return sum(generateur_premiers(debut, fin))


if __name__ == "__main__":
    debut = int(input("Borne inférieure : "))
    fin = int(input("Borne supérieure : "))

    premiers = list(generateur_premiers(debut, fin))
    print(f"Nombres premiers entre {debut} et {fin} : {premiers}")
    print(f"Somme des nombres premiers : {sum(premiers)}")

    # Vérification que somme_premiers utilise bien le générateur
    assert somme_premiers(debut, fin) == sum(premiers)
