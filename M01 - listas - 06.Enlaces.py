def reverse(names):
    left = 0
    right = len(names) - 1
    
    while left < right:
        names[left], names[right] = names[right], names[left]
        left += 1
        right -= 1

names = ['john', 'smith', 'karl']

reverse(names)
print(names) # ['karl', 'smith', 'john']

reverse(names)
print(names) # ['john', 'smith', 'karl']

"""
Explicación paso a paso:

1. La Lógica: La técnica de los "Dos Punteros"
   Imagina que tienes una fila de cartas sobre la mesa y quieres invertir su orden sin levantarlas todas.
   - Pones tu mano izquierda en la primera carta.
   - Pones tu mano derecha en la última carta.
   - Intercambias esas dos cartas de lugar.
   - Mueves tu mano izquierda un paso a la derecha.
   - Mueves tu mano derecha un paso a la izquierda.
   - Repites hasta que tus manos se crucen.

2. El código explicado:
   - `left = 0`: Índice del primer elemento (el principio).
   - `right = len(names) - 1`: Índice del último elemento (nota el -1 porque los índices empiezan en 0).
   - `while left < right`: El ciclo continúa mientras la mano izquierda no haya cruzado a la derecha.
   - `names[left], names[right] = names[right], names[left]`: El Intercambio Mágico de Python (tuple unpacking).
   - `left += 1` y `right -= 1`: Movemos los índices hacia el centro.

3. Visualización en memoria (con ['john', 'smith', 'karl']):
   - Inicio: left=0 ('john'), right=2 ('karl'). ¿0 < 2? Sí. Intercambiamos.
   - Resultado parcial: ['karl', 'smith', 'john'].
   - Movimiento: left sube a 1, right baja a 1.
   - Segunda vuelta: ¿1 < 1? No. El ciclo termina.
"""
