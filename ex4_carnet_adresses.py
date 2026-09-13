"""
Exercice 2.4 : Carnet d'adresses basé sur un dictionnaire.
Permet d'ajouter, supprimer, rechercher et lister les contacts.
Chaque contact est une entrée : nom -> {téléphone, email, entreprise}
"""

carnet = {}


def ajouter_contact(nom, telephone, email, entreprise):
    carnet[nom] = {
        "telephone": telephone,
        "email": email,
        "entreprise": entreprise,
    }
    print(f"Contact '{nom}' ajouté.")


def supprimer_contact(nom):
    if nom in carnet:
        del carnet[nom]
        print(f"Contact '{nom}' supprimé.")
    else:
        print(f"Contact '{nom}' introuvable.")


def rechercher_contact(nom):
    contact = carnet.get(nom)
    if contact:
        print(f"--- {nom} ---")
        for cle, valeur in contact.items():
            print(f"  {cle} : {valeur}")
    else:
        print(f"Contact '{nom}' introuvable.")
    return contact


def afficher_tous():
    if not carnet:
        print("Le carnet d'adresses est vide.")
        return
    print("=== Carnet d'adresses ===")
    for nom, infos in carnet.items():
        print(f"{nom} : {infos}")


if __name__ == "__main__":
    ajouter_contact("Zhang Wei", "138-0000-0001", "zhangwei@xidian.edu.cn", "Xidian University")
    ajouter_contact("Li Na", "139-0000-0002", "lina@example.com", "Huawei")
    ajouter_contact("Wang Fang", "137-0000-0003", "wangfang@example.com", "ZTE")

    afficher_tous()

    print()
    rechercher_contact("Li Na")

    print()
    supprimer_contact("Wang Fang")

    print()
    afficher_tous()
