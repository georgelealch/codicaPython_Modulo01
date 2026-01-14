def compact(coll):
    result = []

    for item in coll:
        if item != None:
            result.append(item)

    return result

print(compact([0, 1, False, None, True, 'wow', None]))
print(compact([]))




def get_same_parity(nums):
    if len(nums) == 0:
        return []

    original_remainder = abs(nums[0]) % 2
    
    result = []

    for num in nums:
        if abs(num) % 2 == original_remainder:
            result.append(num)

    return result

print(get_same_parity([1, 2, 3, 4, 5, 6]))
print(get_same_parity([]))

"""
EXPLICACIÓN DE LOS CAMBIOS:

1. Captura de la paridad inicial:
   'original_remainder = abs(nums[0]) % 2'
   Antes de recorrer la lista, calculamos el resto del primer número. 
   Usamos 'abs()' (valor absoluto) para asegurarnos de trabajar con números positivos
   y evitar confusiones con el operador módulo (%) en números negativos, 
   aunque en Python funciona correctamente.

2. Filtrado dinámico:
   'if abs(num) % 2 == original_remainder:'
   En lugar de buscar siempre números pares (== 0), ahora comparamos 
   contra la paridad del primer elemento que guardamos en 'original_remainder'.
   Así, si el primero era par, filtramos pares. Si era impar, filtramos impares.
"""