def are_symbols_balanced(text):
    stack = []
    
    opening_symbols = ['(', '[', '{', '<']
    closing_symbols = [')', ']', '}', '>']
    
    for char in text:
        if char in opening_symbols:
            stack.append(char)
            
        elif char in closing_symbols:
            if not stack:
                return False
            
            ultimo_abierto = stack.pop()
            
            indice_apertura = opening_symbols.index(ultimo_abierto)
            indice_cierre = closing_symbols.index(char)
            
            if indice_apertura != indice_cierre:
                return False
    
    return len(stack) == 0

print(are_symbols_balanced('(>'))       # False
print(are_symbols_balanced('()'))       # True
print(are_symbols_balanced('[()]'))     # True
print(are_symbols_balanced('({}[])'))   # True
print(are_symbols_balanced('{<>}}'))    # False
print(are_symbols_balanced('([)]'))     # False

"""
Explicación paso a paso de la función are_symbols_balanced:

1.  **Inicialización de la Pila**:
    - Se crea una lista vacía `stack = []`. Esta lista actuará como una pila (LIFO - Last In, First Out), 
    lo que significa que el último elemento que entra es el primero que sale. Esto es fundamental para verificar 
    estructuras anidadas como los paréntesis.

2.  **Definición de Símbolos**:
    - Se definen dos listas: `opening_symbols` para los caracteres de apertura y `closing_symbols` para los de cierre. 
    Es crucial que el orden coincida (el primer elemento de una lista es pareja del primer elemento de la otra).

3.  **Recorrido del Texto**:
    - Se usa un bucle `for` para examinar cada carácter (`char`) de la cadena de entrada `text`.

4.  **Manejo de Aperturas**:
    - Si el carácter actual está en `opening_symbols`, significa que estamos abriendo una nueva estructura. 
    Lo agregamos (`append`) a la pila para recordarlo y verificar su cierre más adelante.

5.  **Manejo de Cierres**:
    - Si el carácter actual está en `closing_symbols`, estamos intentando cerrar una estructura.
    - **Verificación de Pila Vacía**: Antes de nada, si la pila está vacía (`if not stack`), 
    significa que hay un paréntesis de cierre sin uno de apertura previo. La cadena es inválida (`False`).
    - **Validación de Correspondencia**:
        - Se extrae el último paréntesis abierto de la pila con `stack.pop()`.
        - Se busca la posición (índice) de ese paréntesis extraído en la lista de apertura (`opening_symbols.index()`).
        - Se busca la posición del paréntesis de cierre actual en la lista de cierre (`closing_symbols.index()`).
        - Si los índices **no coinciden**, significa que estamos intentando cerrar con un tipo de paréntesis 
        diferente al esperado (por ejemplo, abrir `(` y cerrar `]`). Devolvemos `False`.

6.  **Verificación Final**:
    - Al terminar el bucle, la pila debe estar completamente vacía. 
    Si queda algún elemento (`len(stack) != 0`), significa que hubo paréntesis que se abrieron y nunca se cerraron. 
    Devolvemos `True` solo si la pila está vacía.
"""
