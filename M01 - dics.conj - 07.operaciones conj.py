def diff_keys(old_dict, new_dict):
    old_keys = set(old_dict.keys())
    new_keys = set(new_dict.keys())

    return {
        'kept': old_keys & new_keys,
        'added': new_keys - old_keys,
        'removed': old_keys - new_keys
    }


print(diff_keys({'name': 'Bob', 'age': 42}, {}))
print(diff_keys({}, {'name': 'Bob', 'age': 42}))
print(diff_keys({'a': 2}, {'a': 1}))

"""
--- Explicación Paso a Paso ---

1. **Definición de la función**:
   Definimos `diff_keys(old_dict, new_dict)` que recibe dos diccionarios.

2. **Obtener las claves como conjuntos (sets)**:
   - `old_keys = set(old_dict.keys())`: Extraemos las claves del diccionario antiguo y las convertimos en un conjunto.
   - `new_keys = set(new_dict.keys())`: Hacemos lo mismo para el diccionario nuevo.
   
   ¿Por qué usamos conjuntos (`set`)?
   Porque los conjuntos en Python nos permiten realizar operaciones matemáticas como intersección y diferencia de manera muy eficiente y directa.

3. **Cálculo de las diferencias**:
   - `'kept'`: Usamos el operador `&` (intersección). Esto nos da los elementos que están presentes en AMBOS conjuntos (claves que se mantuvieron).
   - `'added'`: Usamos el operador `-` (diferencia). `new_keys - old_keys` nos da las claves que están en el nuevo pero NO en el antiguo (claves nuevas/agregadas).
   - `'removed'`: Usamos también la diferencia, pero al revés: `old_keys - new_keys`. Esto nos da las claves que estaban en el antiguo pero YA NO están en el nuevo (claves eliminadas).

4. **Retorno del resultado**:
   Devolvemos un diccionario con las tres claves requeridas y sus respectivos conjuntos de resultados.
"""

