def symbole_to_valeur(romain):
    if romain=="I" or romain=="i":
        return 1
    elif romain=="V" or romain=="v":
        return 5
    elif romain=="X" or romain=="x":
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