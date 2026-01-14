from random import randint, choice

def choice_from_range(cadena, in_ini, in_fin):
    # randint(a, b) genera un número entero aleatorio N tal que a <= N <= b.
    # Esto cumple con el requisito de seleccionar un índice dentro del rango (inclusive).
    indice = randint(in_ini, in_fin)
    
    # Obtenemos el carácter en la posición del índice aleatorio.
    letra = cadena[indice]

    # Devolvemos el carácter seleccionado.
    # Es importante usar 'return' para que el valor pueda ser utilizado fuera de la función.
    return letra

# Ejemplo de cómo guardar el resultado en una variable:
# 1. Llamamos a la función y asignamos lo que devuelve (return) a la variable 'caracter_elegido'.
caracter_elegido = choice_from_range("LondonisthecapitalofGreatBritain", 3, 10)

# 2. Ahora podemos usar esa variable para lo que queramos, por ejemplo, imprimirla.
print("El carácter guardado es:", caracter_elegido)
