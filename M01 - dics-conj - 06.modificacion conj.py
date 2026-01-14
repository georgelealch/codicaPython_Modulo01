def toggle(flag, flags_set):
    """
    Cambia el estado de una bandera en un conjunto (in-place).
    Si la bandera está, la elimina. Si no está, la agrega.
    """
    if flag in flags_set:
        flags_set.remove(flag)
    else:
        flags_set.add(flag)

def toggled(flag, flags_set):
    """
    Devuelve un NUEVO conjunto con el estado de la bandera cambiado.
    No modifica el conjunto original.
    """
    # Creamos una copia del conjunto original para no modificarlo
    new_flags = flags_set.copy()
    
    if flag in new_flags:
        new_flags.remove(flag)
    else:
        new_flags.add(flag)
    return new_flags

# --- Verificación (puedes ejecutar esto para probar) ---
if __name__ == '__main__':
    READ_ONLY = 'read_only'
    flags = set()
    toggle(READ_ONLY, flags)
    print(f"Después de toggle: {READ_ONLY in flags}") # Debería ser True
    
    toggle(READ_ONLY, flags)
    print(f"Después de segundo toggle: {READ_ONLY in flags}") # Debería ser False

    new_flags = toggled(READ_ONLY, flags)
    print(f"Original flags: {READ_ONLY in flags}") # False
    print(f"New flags: {READ_ONLY in new_flags}") # True

"""
Explicación Paso a Paso:

1. Función toggle(flag, flags_set):
   - Esta función modifica el conjunto `flags_set` directamente (in-place).
   - Primero, verificamos si la `flag` ya existe en `flags_set` usando el operador `in`.
   - Si `flag in flags_set` es True (la bandera está presente), usamos el método `.remove(flag)` para quitarla del conjunto.
   - Si la bandera NO está presente (`else`), usamos el método `.add(flag)` para agregarla al conjunto.
   - No retornamos nada (None) porque el cambio se hace directamente sobre el objeto conjunto original.

2. Función toggled(flag, flags_set):
   - Esta función debe devolver un *nuevo* conjunto y dejar el original intacto.
   - Paso crucial: `new_flags = flags_set.copy()`. Creamos una copia superficial del conjunto original. 
   Si trabajamos directamente sobre `flags_set`, estaríamos modificando el original (como en `toggle`), lo cual no queremos aquí.
   - Luego, aplicamos la misma lógica que en `toggle`, pero sobre `new_flags`:
     - Si la bandera está en `new_flags`, la removemos (`remove`).
     - Si no está, la agregamos (`add`).
   - Finalmente, retornamos `new_flags`, que es el nuevo conjunto con el cambio aplicado.
"""