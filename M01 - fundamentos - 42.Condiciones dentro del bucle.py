################ EJERCICIO LECCION ######################

def has_char(cadena, letra):
    i = 0
    cadena = cadena.lower()

    while i < len(cadena):
        if cadena[i] == letra.lower():
            return True
        i += 1

    return False

print(has_char("Alex", "s"))








################### EJEMPLO 1 PARA BUSCAR @ ####################

def count_chars(texto, letra):
    i = 0               # Empezamos desde el primer carácter
    contador = 0        # Inicializamos el contador en 0

    while i < len(texto):                # Recorremos el texto letra por letra
        if texto[i] == letra:            # Si la letra actual coincide con la que buscamos
            contador += 1                # Aumentamos el contador
        i += 1                           # Pasamos a la siguiente letra

    return contador

print(count_chars("alexleal@@@jumail.com", "@"))


def es_email_valido(email):
    return count_chars(email, '@') == 1  # Es válido si hay exactamente un solo '@'

print(es_email_valido('arya@@stark.com')) 