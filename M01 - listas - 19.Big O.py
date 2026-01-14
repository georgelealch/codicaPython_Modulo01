'''
def get_intersection_of_sorted_lists(list1, list2):
    l1_index = 0
    l2_index = 0
    intersection = []
    
    while l1_index < len(list1) and l2_index < len(list2):
        if list1[l1_index] == list2[l2_index]:
            intersection.append(list1[l1_index])
            l1_index += 1
            l2_index += 1
        elif list1[l1_index] < list2[l2_index]:
            l1_index += 1
        else:
            l2_index += 1
    
    return list(set(intersection))

print(get_intersection_of_sorted_lists([10, 11, 24], [10, 13, 14, 18, 24, 30]))
print(get_intersection_of_sorted_lists([10, 11, 24], [-2, 3, 4]))
print(get_intersection_of_sorted_lists([], [2]))
print(get_intersection_of_sorted_lists([1, 2, 2, 3, 4], [2, 2, 3, 5])) # [2, 3]
print(get_intersection_of_sorted_lists([1, 1, 1, 2, 2, 2], [1, 1, 2, 2, 3, 3])) # [1, 2]
'''


def get_intersection_of_sorted_lists_2(list1, list2):
    l1_index = 0
    l2_index = 0
    intersection = []
    
    while l1_index < len(list1) and l2_index < len(list2):
        if list1[l1_index] == list2[l2_index]:
            # Verificamos si la lista está vacía o si el último elemento es distinto al actual
            # para evitar duplicados sin usar set()
            if not intersection or intersection[-1] != list1[l1_index]:
                intersection.append(list1[l1_index])
            l1_index += 1
            l2_index += 1
        elif list1[l1_index] < list2[l2_index]:
            l1_index += 1
        else:
            l2_index += 1
    
    return intersection

print("\n--- Resultados Nueva Función ---")
print(get_intersection_of_sorted_lists_2([10, 11, 24], [10, 13, 14, 18, 24, 30]))
print(get_intersection_of_sorted_lists_2([10, 11, 24], [-2, 3, 4]))
print(get_intersection_of_sorted_lists_2([], [2]))
print(get_intersection_of_sorted_lists_2([1, 2, 2, 3, 4], [2, 2, 3, 5])) 
print(get_intersection_of_sorted_lists_2([1, 1, 1, 2, 2, 2], [1, 1, 2, 2, 3, 3]))

"""
Explicación paso a paso de las modificaciones:

1.  **Creación de una nueva función (`get_intersection_of_sorted_lists_2`):**
    Para no alterar tu código original, he creado una nueva versión que implementa las mejoras sin usar `set()`.

2.  **Eliminación de `set()`:**
    La función original usaba `return list(set(intersection))` para eliminar duplicados. 
    *   **Por qué cambiarlo:** Aunque `set` elimina duplicados, no garantiza mantener el orden de los elementos. Además, convertir a conjunto y luego a lista añade pasos extra.
    Dado que nuestras listas de entrada ya están ordenadas, podemos construir el resultado limpio y ordenado directamente.

3.  **Manejo de duplicados dentro del bucle:**
    En lugar de limpiar al final, añadí la condición: 
    `if not intersection or intersection[-1] != list1[l1_index]:`
    *   **Cómo funciona:** Antes de agregar un número coincidente, verificamos dos cosas:
        a. `not intersection`: ¿Es el primer elemento que vamos a agregar? (Si la lista está vacía, seguro no hay duplicado previo).
        b. `intersection[-1] != list1[l1_index]`: ¿Es este número diferente al último que agregamos?
        Solo si se cumple alguna de estas, agregamos el número. Si es igual al último (ej. otro 2 después de un 2), simplemente avanzamos los índices sin agregarlo.
    *   **Beneficio:** Esto mantiene la lista de intersección siempre libre de duplicados y ordenada, de forma eficiente y paso a paso.

4.  **Complejidad O(n + m):**
    El algoritmo usa dos índices (`l1_index` y `l2_index`) que recorren cada lista una sola vez de principio a fin.
    *   Si los elementos son iguales, avanzamos ambos.
    *   Si uno es menor, avanzamos solo ese índice para "alcanzar" al otro.
    Nunca retrocedemos. Por tanto, el número máximo de pasos es la suma de los tamaños de ambas listas (n + m), lo cual es ideal y mucho más rápido que comparar cada elemento de una lista con todos los de la otra (O(n * m)).
"""