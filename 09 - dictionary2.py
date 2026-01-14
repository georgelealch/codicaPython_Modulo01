def collect_indexes(collection):
    indices = {}
    for index, element in enumerate(collection):
        if element in indices:
            indices[element].append(index)
        else:
            indices[element] = [index]
    return indices

print(collect_indexes("hello"))
print(collect_indexes([1, 2, 2, 4, 5, 7, 7, 7, 9, 10]))

# Explicación paso a paso de la función 'collect_indexes':
#
# 1. Definición de la función:
#    - `def collect_indexes(collection):` define una función que recibe un argumento llamado `collection`.
#      Esta colección puede ser una cadena de texto, una lista, o cualquier otro objeto iterable.
#
# 2. Inicialización del diccionario:
#    - `indices = {}` crea un diccionario vacío donde guardaremos los resultados.
#      Las claves serán los elementos de la colección y los valores serán listas de índices.
#
# 3. Iteración con enumerate (La parte clave):
#    - `for index, element in enumerate(collection):`
#    - ¿Qué hace `enumerate()`?
#      Normalmente, un bucle `for item in lista` solo te da el elemento, pero no su posición (índice).
#      `enumerate(collection)` toma tu colección y te "enumera" sus elementos, devolviéndote dos cosas a la vez en cada paso:
#         1. La posición (índice) donde estamos (empezando desde 0).
#         2. El elemento en sí.
#    - Ejemplo visual:
#      Si la colección es `['a', 'b', 'c']`, `enumerate` generará:
#      Vuelta 1: index = 0, element = 'a'
#      Vuelta 2: index = 1, element = 'b'
#      Vuelta 3: index = 2, element = 'c'
#    - Por eso escribimos `for index, element ...`:
#      estamos "desempaquetando" esos dos valores en dos variables separadas para usarlas dentro del bucle.
#
# 4. Verificación y actualización:
#    - `if element in indices:` comprueba si el elemento ya está registrado como clave en nuestro diccionario.
#    - Si ya existe (`True`), significa que hemos visto este elemento antes. Entonces:
#      `indices[element].append(index)` agrega el índice actual a la lista de índices existente para ese elemento.
#    - `else:` (si no existe), es la primera vez que vemos este elemento. Entonces:
#      `indices[element] = [index]` crea una nueva entrada en el diccionario. 
#       La clave es el elemento y el valor es una lista nueva que contiene el índice actual.
#
# 5. Retorno del resultado:
#    - `return indices` devuelve el diccionario completo una vez que el bucle ha terminado de recorrer toda la colección.