def all_unique(iterable):
    seen = set()
    for element in iterable:
        if element in seen:
            return False
        seen.add(element)
    return True

# Ejemplos de uso del ejercicio
print(all_unique([]))                # True
print(all_unique([1, 2, 3]))         # True
print(all_unique(iter([1, 2, 3])))   # True
print(all_unique([1, 2, 1]))         # False

# Explicación paso a paso:
# 1. Definimos la función `all_unique` que acepta un argumento `iterable`. 
#    Este puede ser una lista, un generador, o cualquier objeto sobre el que se pueda iterar.
#
# 2. Inicializamos un conjunto vacío llamado `seen` (visto). 
#    Los conjuntos (sets) en Python son muy eficientes para verificar si un elemento existe dentro de ellos.
#
# 3. Iniciamos un bucle `for` para recorrer cada `element` en el `iterable`.
#
# 4. Dentro del bucle, verificamos: `if element in seen:`.
#    Si el elemento actual ya está en nuestro conjunto `seen`, significa que es un duplicado.
#    En ese caso, retornamos `False` inmediatamente. Esto hace que la función sea eficiente, 
#    ya que se detiene apenas encuentra una repetición.
#
# 5. Si el elemento no estaba en el conjunto, lo agregamos usando `seen.add(element)`.
#    Esto registra que ya hemos "visto" este elemento.
#
# 6. Si el bucle termina de recorrer todos los elementos sin haber retornado `False`, 
#    significa que no se encontraron duplicados. Por lo tanto, retornamos `True`.