
def rotated_left(cadena):
    return cadena[1:] + cadena[:1]


print(rotated_left("ABCDE"))


def rotated_right(lista):
    return lista[-1:] + lista[:-1]


print(rotated_right([1, 2, 3, 4, 5]))


"""
l = [1, 2, 3, 4, 5, 6]
l[::2] = [0, 0, 0]
print(l)



ldos = [1, 2, 3, 4, 5]
n = 2
ldos == l[:n] + l[n:]
print(ldos)


ltres = [1, 2, 3, 4, 5, 6]
ltres[::2] = ltres[1::2]
print(ltres)


s = 'ABRAKADABRA'
print(s[6:1::-1])





¡Claro que sí! Aquí te explico detalladamente por qué hice esos cambios.

El objetivo principal era que las funciones sirvieran para cadenas, listas y tuplas sin necesidad de código extra.

1. El problema de 

rotated_left
En tu código original tenías esto:

cadena[1::] + cadena[0]
Esto funcionaba bien para cadenas ("A" + "B" es válido), pero fallaba con listas.

El error: Si tienes una lista [1, 2, 3]:
lista[1:] devuelve [2, 3] (una lista).
lista[0] devuelve 1 (un entero).
Al intentar sumar [2, 3] + 1, Python arroja un error (TypeError) porque no puedes sumar una lista con un número.
2. La solución: "Slicing" (Rebanado)
Cambié el código a:

cadena[1:] + cadena[:1]
La clave está en usar [:1] en lugar de [0].

¿La diferencia?
lista[0] extrae el elemento crudo (1).
lista[:1] crea una nueva lista que contiene ese elemento ([1]).
Ahora la suma es: [2, 3] + [1]. Como ambos son listas, Python los concatena perfectamente resultando en [2, 3, 1]. Lo mismo aplica para tuplas y cadenas.

3. Limpieza en 

rotated_right
Para 

rotated_right
, tu lógica lista[-1::] ya funcionaba porque al usar los dos puntos (:) Python devuelve una lista/segmento, no un elemento suelto.

Sin embargo, lo simplifiqué para que fuera más legible y consistente con la otra función:

# Tu versión
lista[-1::] + lista[0:-1]
# Mi versión (más limpia)
lista[-1:] + lista[:-1]
Ambas hacen lo mismo: toman el último trozo (como lista) y lo ponen al principio.

Resumen: Al usar siempre [:] (segmentación), garantizamos que nunca estamos trabajando con elementos sueltos, sino siempre con "trozos" del mismo tipo que el original, permitiendo que la suma funcione para cualquier secuencia.
"""

