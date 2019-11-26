def un_symbole_to_valeur(romain):
    if romain == "I" or romain == "i":
        return 1
    elif romain == "V" or romain == "v":
        return 5
    elif romain == "X" or romain == "x":
        return 10
    elif romain == "L" or romain == "l":
        return 50
    elif romain == "C" or romain == "c":
        return 100
    elif romain == "D" or romain == "d":
        return 500
    elif romain == "M" or romain == "m":
        return 1000
    else:
        return "error"


def deux_symboles_identiques_to_valeur(romains):
    if romains == "II" or romains == "ii":
        return 2
    elif romains == "VV" or romains == "vv":
        return 10
    elif romains == "XX" or romains == "xx":
        return 20
    elif romains == "LL" or romains == "ll":
        return 100
    elif romains == "CC" or romains == "cc":
        return 200
    elif romains == "DD" or romains == "dd":
        return 1000
    elif romains == "MM" or romains == "mm":
        return 2000
    else:
        return "error"


def chaine_d_identiques(chaine):
    indice_caractere_precedent = 0
    indice_caractere_suivant = 1
    identiques = False

    while indice_caractere_suivant < len(chaine):
        if chaine[indice_caractere_suivant] == chaine[indice_caractere_precedent]:
            identiques = True
            indice_caractere_precedent += 1
            indice_caractere_suivant += 1
        else:
            return False

    return identiques


def n_symboles_identiques_to_valeur(romains):
    if chaine_d_identiques(romains):
        somme_identiques = 0
        for i in range(len(romains)):
            somme_identiques += un_symbole_to_valeur(romains[i])
        return somme_identiques
    else:
        return "error"

