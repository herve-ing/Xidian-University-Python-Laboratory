"""
Exercice 2.3 : Fonction simulant le comportement de sorted() (tri fusion),
avec prise en charge des paramètres 'key' et 'reverse', comme l'original.
"""


def mon_sorted(iterable, key=None, reverse=False):
    """Réimplémentation de sorted() en utilisant l'algorithme du tri fusion."""
    elements = list(iterable)
    if key is None:
        key = lambda x: x

    def fusion(gauche, droite):
        resultat = []
        i = j = 0
        while i < len(gauche) and j < len(droite):
            if key(gauche[i]) <= key(droite[j]):
                resultat.append(gauche[i])
                i += 1
            else:
                resultat.append(droite[j])
                j += 1
        resultat.extend(gauche[i:])
        resultat.extend(droite[j:])
        return resultat

    def tri_fusion(liste):
        if len(liste) <= 1:
            return liste
        milieu = len(liste) // 2
        gauche = tri_fusion(liste[:milieu])
        droite = tri_fusion(liste[milieu:])
        return fusion(gauche, droite)

    resultat = tri_fusion(elements)
    if reverse:
        resultat.reverse()
    return resultat


if __name__ == "__main__":
    donnees = [5, 2, 9, 1, 5, 6, -3, 0]
    print("Liste originale       :", donnees)
    print("mon_sorted            :", mon_sorted(donnees))
    print("sorted (référence)    :", sorted(donnees))
    print("mon_sorted (reverse)  :", mon_sorted(donnees, reverse=True))

    mots = ["banane", "kiwi", "abricot", "pomme"]
    print("\nTri par longueur de mot :")
    print("mon_sorted :", mon_sorted(mots, key=len))
    print("sorted     :", sorted(mots, key=len))

    # Vérification automatique de cohérence
    assert mon_sorted(donnees) == sorted(donnees)
    assert mon_sorted(mots, key=len) == sorted(mots, key=len)
    print("\nVérification : mon_sorted == sorted -> OK")
