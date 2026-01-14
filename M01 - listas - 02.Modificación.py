def swap(lista):
    if len(lista) < 2:
        return lista
    
    lista[0], lista[-1] = lista[-1], lista[0]
    return lista

print(swap(['one', 'two', 'three']))
print(swap(['one', 'two']))
print(swap(['one']))
print(swap([]))


def get(lista, ind, default=None):
    if -len(lista) <= ind < len(lista):
        return lista[ind] # ← devolvemos el elemento
    return default # ← devolvemos el valor por defecto

cities = ['moscow', 'london', 'berlin', 'porto', '', True]
print(get(cities, 1, 'paris'))


"""
Esa es la magia de las funciones: la generalización.

Para Python, nombres como lista o cities son solo etiquetas. La conexión ocurre en el momento en que llamas a la función.

Piénsalo así:

La Definición (def get(lista, ...)): Aquí le estás diciendo a Python: "Oye, voy a crear una máquina llamada 

get
. Esta máquina tiene una ranura de entrada a la que llamaré lista. No sé qué me van a meter ahí todavía, pero sea lo que sea, dentro de mi máquina lo llamaré lista".

lista es solo un nombre interno (un parámetro).
La Llamada (

get(cities, ...)
): Aquí es donde ocurre el vínculo. Cuando escribes 

get(cities, ...)
, Python hace esto internamente antes de ejecutar el código de la función:

lista = cities
Le estás diciendo: "Toma mi variable cities y métela en la ranura lista de la máquina".

¿Por qué es útil esto? Porque ahora tu función no está "casada" con cities. Puedes reutilizarla con cualquier otra lista sin cambiar ni una línea de código dentro de la función:

numeros = [1, 2, 3]
get(numeros, 1)  # Aquí, internamente: lista = numeros
nombres = ["Ana", "Juan"]
get(nombres, 0)  # Aquí, internamente: lista = nombres
Si la función usara la palabra cities dentro, solo serviría para esa lista específica y perdería toda su utilidad como herramienta general.
"""