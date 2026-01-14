def bubble_sort_example(coll):
    steps_count = len(coll) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(steps_count):
            if coll[i] > coll[i + 1]:
                coll[i], coll[i + 1] = coll[i + 1], coll[i]
                swapped = True
        
        steps_count -= 1

    return coll

print(bubble_sort_example([3, 2, 10, -2, 0]))

# EXPLICACIÓN DE LA FUNCIÓN:
#
# Esta función implementa el algoritmo "Bubble Sort" (ordenamiento de burbuja) para ordenar una lista.
#
# 1. Por qué 'steps_count' usa 'len(coll) - 1':
#    La lista tiene 'len(coll)' elementos. Si queremos comparar cada elemento con su vecino (i con i+1),
#    no podemos llegar al último elemento porque no tiene vecino a su derecha.
#    Por ejemplo, si hay 5 elementos, el último índice es 4. Si intentamos acceder a índice 4+1 (5), daría error.
#    Por eso el límite es el penúltimo índice (len - 1).
#
# 2. El bucle 'for i in range(steps_count)':
#    Recorre la lista paso a paso. En cada iteración, 'i' es la posición actual.
#
# 3. Por qué el '+1' en 'coll[i+1]':
#    Se usa para mirar el siguiente elemento en la lista.
#    'coll[i] > coll[i + 1]' pregunta: "¿Es el elemento actual mayor que el siguiente?"
#    Si es así, están en el orden incorrecto y deben intercambiarse.
#
# 4. 'steps_count -= 1':
#    Después de cada pasada completa del bucle 'for', el número más grande se habrá movido al final
#    de la lista (burbujea hasta el tope).
#    En la siguiente vuelta, ya no hace falta revisar esa última posición porque ya está ordenada,
#    así que reducimos el rango en 1 para ser más eficientes.

def bubble_sort(coll):
    steps_count = len(coll) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(steps_count):
            if coll[i] > coll[i + 1]:
                coll[i], coll[i + 1] = coll[i + 1], coll[i]
                swapped = True
        
        steps_count -= 1

    return coll

print(bubble_sort([3, 10, 4, 3]))

# EXPLICACIÓN DE LA FUNCIÓN:
