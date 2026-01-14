def difference(base_list, *other_lists):
    # Copiamos la lista base (para no modificar el original)
    diff_result = base_list[:]

    # Recorremos cada lista "contraria"
    for current_list in other_lists:
        new_diff = []
        for item in diff_result:
            # Solo guardamos los que NO están en la lista actual
            if item not in current_list:
                new_diff.append(item)
        # Actualizamos el resultado parcial
        diff_result = new_diff

    return diff_result


tasks1 = ['reportes', 'presentación', 'revisión']
tasks2 = ['presentación', 'diseño']

print(difference(tasks1, tasks2)) 



list1 = [1, 2, 3]
list2 = [4, 3, 6, 1, 5]

print(set(list1) & set(list2))  # intersección -> {1, 3}
print(set(list1) | set(list2))  # unión -> {1, 2, 3, 4, 5, 6}
print(set(list1) - set(list2))  # diferencia -> {2}

'''
Un conjunto es una colección de elementos únicos.
Intersección: lo que está en todas las listas (sirve para encontrar coincidencias).
Unión: todos los elementos juntos, sin duplicados (sirve para combinar resultados).
Diferencia: lo que está en la primera lista pero no en la segunda (sirve para detectar lo exclusivo).
Con el operador in podemos comprobar si un elemento pertenece a una lista.
'''

