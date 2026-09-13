"""
Exercice 1.6 : L'utilisateur saisit une année (4 chiffres),
le programme indique si c'est une année bissextile.

Règle : bissextile si divisible par 400,
         OU (divisible par 4 ET non divisible par 100).
"""


def est_bissextile(annee: int) -> bool:
    if annee % 400 == 0:
        return True
    if annee % 4 == 0 and annee % 100 != 0:
        return True
    return False


def main():
    while True:
        saisie = input("Entrez une année (4 chiffres, 'q' pour quitter) : ").strip()
        if saisie.lower() == "q":
            break
        if not saisie.isdigit() or len(saisie) != 4:
            print("Veuillez entrer une année valide sur 4 chiffres.")
            continue

        annee = int(saisie)
        if est_bissextile(annee):
            print(f"{annee} est une année bissextile.")
        else:
            print(f"{annee} n'est PAS une année bissextile.")


if __name__ == "__main__":
    main()
