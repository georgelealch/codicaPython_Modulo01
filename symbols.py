
def is_vowel(cadena):
    i = 0
    cadena = cadena.lower()

    while i < len(cadena):
        if cadena[i] in ["a", "e", "i", "o", "u"]:
            return True
        i += 1
    return False
    