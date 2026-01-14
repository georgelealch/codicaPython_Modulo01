fruit = ['apple', 'orange', 'banana', 'pineapple']
prim, sec, *ulti = fruit

rest = fruit[1:]
rest2 = fruit[:-2]

print(prim)
print(sec)
print(ulti)
print(rest)
print(rest2)


def get_max(list):
    list = list

    if list == [] or len(list) == 1:
        return None
    
    firts, *rest = list  # ESTE ANTES ESTABA ARRIBA, ANTES DEL 'IF LIST == []... PERO ASÍ ESTABA MAL, POR LA EXPLICACIÓN DE ABAJO'
    max = firts    
    for i in rest:
        if i > max:
            max = i
    return max

print(get_max([1, 10, 8]))


def get_max_v2(numbers):
    if not numbers:
        return None

    # Usamos desestructuración con rest para separar el primero del resto
    first, *rest = numbers
    max_val = first

    for n in rest:
        if n > max_val:
            max_val = n
            
    return max_val

print(get_max_v2([-1, -2, -3]))

"""
Explicación paso a paso de los cambios:

1.  **Manejo de lista vacía**: 
    Lo primero que hacemos es verificar `if not numbers:`. Esto es fundamental validarlo ANTES de intentar desestructurar, ya que hacer `first, *rest = []` lanzaría un error porque no hay elementos para asignar a `first`.

2.  **Desestructuración con Operador Rest (*)**:
    La línea `first, *rest = numbers` hace dos cosas al mismo tiempo:
    -   Asigna el primer elemento de la lista a la variable `first`.
    -   El operador `*` (rest) agrupa todos los elementos restantes en una nueva lista llamada `rest`.
    Esto nos permite inicializar nuestro valor máximo (`max_val`) con el primer elemento (`first`) y tener lista la sub-lista (`rest`) para iterar.

3.  **Búcle Simplificado**:
    Iteramos solo sobre `rest`. Como ya tenemos el primer elemento considerado en `max_val`, no necesitamos volver a revisarlo. Comparamos cada número `n` con `max_val` y actualizamos si encontramos uno mayor.

Este enfoque es más limpio y "Pythonico" que el original porque evita el uso de índices manuales y aprovecha las características modernas del lenguaje.
"""