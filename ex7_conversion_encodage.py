"""
Exercice 1.7 : L'utilisateur saisit un nom de fichier et son encodage.
Le programme lit le fichier puis le réenregistre en UTF-8.
"""
import sys


def convertir_en_utf8(nom_fichier: str, encodage_source: str) -> str:
    with open(nom_fichier, "r", encoding=encodage_source) as f:
        contenu = f.read()

    nom_sortie = nom_fichier + ".utf8.txt"
    with open(nom_sortie, "w", encoding="utf-8") as f:
        f.write(contenu)

    return nom_sortie


def main():
    nom_fichier = input("Nom du fichier à lire : ").strip()
    encodage_source = input("Encodage du fichier (ex: gbk, gb2312, latin-1) : ").strip()

    try:
        nom_sortie = convertir_en_utf8(nom_fichier, encodage_source)
        print(f"Conversion réussie ! Fichier UTF-8 créé : {nom_sortie}")
    except FileNotFoundError:
        print(f"Erreur : le fichier '{nom_fichier}' est introuvable.")
    except LookupError:
        print(f"Erreur : l'encodage '{encodage_source}' n'est pas reconnu.")
    except UnicodeDecodeError:
        print("Erreur : impossible de décoder le fichier avec l'encodage indiqué.")
        sys.exit(1)


if __name__ == "__main__":
    main()
