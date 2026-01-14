schools = ['Códica', 'codeacademy']

first, second, *rest = ['youtube', 'teamtreehouse', *schools, 'codeschool']

print(rest)


def flatten(coll):
    new_list = []

    for element in coll:
        if isinstance(element, list):
            # Si el elemento es una lista, desplegamos su contenido junto con lo que ya llevamos
            new_list = [*new_list, *element]
        else:
            # Si no es una lista, desplegamos lo que llevamos y agregamos el elemento nuevo al final
            new_list = [*new_list, element]
    
    return new_list

print(flatten([]))
print(flatten([1, [3, 2], 9]))
print(flatten([1, [[2], [3]], [9]]))

# Explicación paso a paso:
# 1. Definimos la función 'flatten' que recibe la colección 'coll'.
# 2. Inicializamos 'new_list' como una lista vacía para ir construyendo el resultado.
# 3. Iteramos elemento por elemento sobre la lista 'coll'.
# 4. Verificamos si el 'element' actual es de tipo lista usando isinstance(element, list).
# 5. Si es una lista, usamos el operador spread (*) dos veces:
#    - *new_list: para mantener los elementos que ya habíamos acumulado.
#    - *element: para sacar los elementos de la sub-lista y ponerlos al mismo nivel.
#    Esto efectivamente 'aplana' ese nivel de anidamiento.
# 6. Si el elemento no es una lista, igual reconstruimos la lista con *new_list y agregamos el 'element' simple al final.
# 7. Retornamos la 'new_list' resultante que ahora tiene un nivel menos de profundidad.
