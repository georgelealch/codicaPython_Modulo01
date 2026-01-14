def unique(collection):
    seen = set()
    unique_items = []
    for item in collection:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items


def get_same_count(list1, list2):
    count = 0
    unique_list1 = unique(list1)
    unique_list2 = unique(list2)

    for item1 in unique_list1:
        for item2 in unique_list2:
            if item1 == item2:
                count += 1
    
    return count

print(get_same_count([1, 3, 2, 2], [3, 1, 1, 2, 5]))

"""
EXPLICACIÓN PASO A PASO:

1. Función unique(collection):
   - Esta función recibe una lista (collection).
   - Crea un conjunto vacío 'seen' para registrar qué elementos ya hemos visto.
   - Crea una lista vacía 'unique_items' para guardar los elementos únicos en orden de aparición.
   - Recorre cada item de la colección:
     - Si el item no está en 'seen', significa que es nuevo. Lo agrega a 'seen' y a 'unique_items'.
     - Si ya está en 'seen', lo ignora.
   - Retorna la lista 'unique_items' sin duplicados.

2. Función get_same_count(list1, list2):
   - Recibe dos listas que pueden tener elementos repetidos.
   - Primero llama a 'unique()' para obtener las versiones sin duplicados de ambas listas (unique_list1 y unique_list2).
   - Inicializa una variable 'count' en 0 para contar las coincidencias.
   - Utiliza dos bucles anidados (un bucle dentro de otro):
     - El ciclo externo recorre cada elemento de unique_list1.
     - El ciclo interno recorre cada elemento de unique_list2.
     - Si encuentra que los elementos son iguales, incrementa 'count' en 1.
   - Al final, retorna 'count', que representa la cantidad de valores únicos compartidos.

Relación:
La función get_same_count utiliza la función unique como una herramienta auxiliar (helper) para simplificar los 
datos antes de procesarlos. Sin unique, tendríamos que manejar los duplicados dentro de la lógica de conteo, 
lo cual sería más complejo.
""" 