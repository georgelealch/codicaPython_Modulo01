def apply_diff(target, diff):
    if 'add' in diff:
        target.update(diff['add'])
    if 'remove' in diff:
        target.difference_update(diff['remove'])

# Test code
target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print(target)  # => {'c', 'b'}

# Explicación paso a paso:
# 1. Definimos la función `apply_diff` que acepta dos argumentos: `target` (el conjunto a modificar) y `diff` (el diccionario con los cambios).
# 2. Verificamos si la clave 'add' existe en el diccionario `diff` usando `if 'add' in diff:`.
# 3. Si existe, usamos el método `update()` del conjunto `target`. 
#    Este método añade todos los elementos del conjunto `diff['add']` al conjunto `target` de una sola vez. Es equivalente a hacer una unión in-place (|=).
# 4. A continuación, verificamos si la clave 'remove' existe en el diccionario `diff` usando `if 'remove' in diff:`.
# 5. Si existe, usamos el método `difference_update()` del conjunto `target`. Este método elimina todos los elementos presentes en `diff['remove']` del conjunto `target`. 
#    Es equivalente a hacer una resta de conjuntos in-place (-=).
# 6. La función no retorna nada explícitamente (retorna None), ya que modifica el objeto `target` original directamente ("in-place").
# 7. Finalmente, probamos la función con el ejemplo dado. El conjunto 'target' original {'a', 'b'} se actualiza: se añade 'c' (quedando {'a', 'b', 'c'}) 
#    y luego se elimina 'a', resultando en {'b', 'c'}.


print('Num. probabilidad')
p = 1
for i in range(1, 80):
    p = p * (366 - i) / 365
    print(f'{i}: {(1-p):.3f}')